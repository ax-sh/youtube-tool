from typing import Literal, Optional, List, Any

from pydantic import BaseModel, model_validator, HttpUrl

CookiesBrowsers = Literal["brave", "chrome", "vivaldi", "firefox", ""]


class YoutubeVideo(BaseModel):
    id: str
    url: HttpUrl
    title: str
    view_count: int = 0
    duration: int = 0
    thumbnails: List[Any] = []
    timestamp: int = 0

    @model_validator(mode="before")
    @classmethod
    def normalize_thumbnail(cls, data: Any) -> Any:
        thumbnails = data["thumbnails"]
        thumb = max(thumbnails, key=lambda x: x["height"] * x["width"])
        data["thumb"] = thumb["url"]

        return data

    thumb: str = ""

    # channel_id: str = ""
    # channel_url: str = ""
    # channel: str = ""
    # uploader: str = ""
    # uploader_id: str = ""
    # uploader_url: str = ""
    # release_timestamp: str = ""
    # availability: str = ""
    # live_status: str = ""
    # channel_is_verified: str = ""
    # __x_forwarded_for_ip: str = ""

    class Config:
        extra = "allow"


class YoutubePlaylist(BaseModel):
    channel_url: str
    channel_id: str
    channel: str
    availability: str

    entries: List[YoutubeVideo]

    class Config:
        extra = "allow"


class PlaylistEntry(BaseModel):
    title: str

    class Config:
        extra = "allow"


class VideoInfo(BaseModel):
    description: Optional[str]
    uploader: str
    uploader_id: str
    uploader_url: HttpUrl
    release_timestamp: Optional[str]
    availability: Optional[str]
    live_status: Optional[str]
    channel_is_verified: Optional[bool]
    __x_forwarded_for_ip: Optional[str]
