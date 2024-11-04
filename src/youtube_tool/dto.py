from typing import Any

from pydantic import BaseModel, field_validator
from datetime import datetime


class VideoDTO(BaseModel):
    id: str
    title: str
    url: str
    view_count: int
    timestamp: datetime

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
        else:
            raise ValueError(
                "Invalid timestamp format. Expected an integer, string, or datetime object."
            )

    # @field_validator("name")
    # @classmethod
    # def name_must_contain_space(cls, v: str) -> str:
    #     if " " not in v:
    #         raise ValueError("must contain a space")
    #     return v.title()


# @field_validator("timestamp", pre=True)
# def parse_timestamp(cls, value):
#     # Define a custom format if needed
#     return (
#         datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
#         if isinstance(value, str)
#         else value
#     )


def playlist_dto(data):
    entries = data["entries"]
    dto = []
    for entry in entries:
        dto.append(VideoDTO(**entry))
    return dto
