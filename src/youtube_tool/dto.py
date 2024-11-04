from typing import List, Any, Optional
from enum import Enum
from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class VideoStatus(Enum):
    NON_ACCESSIBLE = "NON_ACCESSIBLE"
    UNKNOWN = "UNKNOWN"
    AVAILABLE = "AVAILABLE"


class VideoDTO(BaseModel):
    id: str
    title: str
    url: str
    view_count: Optional[int] = 0
    duration: Optional[int] = 0
    timestamp: Optional[datetime]
    channel_id: Optional[str]
    channel: Optional[str]
    video_status: Optional[VideoStatus] = VideoStatus.UNKNOWN

    @field_validator("timestamp", mode="before")
    def ensure_timestamp_is_datetime(cls, value: Any) -> datetime:
        # If the timestamp is an integer, convert it to a datetime object
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        elif isinstance(value, str):
            # Attempt to parse the timestamp if it's a string
            return datetime.fromisoformat(value)
        elif isinstance(value, datetime):
            return value  # Already a datetime, return as is
        elif value is None:
            return value
        else:
            raise ValueError(
                "Invalid timestamp format. Expected an integer, string, or datetime object."
            )

    @model_validator(mode="before")
    def check_release_date(cls, values):
        title = values.get("title")
        NON_ACCESSABLE = ["[Deleted video]", "[Private video]"]
        values["video_status"] = (
            VideoStatus.AVAILABLE
            if title in NON_ACCESSABLE
            else VideoStatus.NON_ACCESSIBLE
        )

        return values

    thumbnails: List[Any] = []
    thumb: str = ""

    @model_validator(mode="before")
    def normalize_thumbnail(cls, data: Any) -> Any:
        thumbnails = data.get("thumbnails")
        thumb = max(thumbnails, key=lambda x: x.get("height", 1) * x.get("width", 1))
        data["thumb"] = thumb["url"]

        return data


def playlist_dto(data):
    entries = data["entries"]
    dto = []
    for entry in entries:
        dto.append(VideoDTO(**entry))
    return dto
