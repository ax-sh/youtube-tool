from typing import Literal, Optional, List, Any

from pydantic import BaseModel, model_validator, HttpUrl, ConfigDict

CookiesBrowsers = Literal["brave", "chrome", "vivaldi", "firefox", "safari", ""]


class YoutubeVideo(BaseModel):
    id: str
    url: HttpUrl
    title: str
    view_count: Optional[int] = None
    duration: Optional[int] = None
    timestamp: Optional[int] = None
    thumbnails: List[Any] = []

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

    # Using ConfigDict to set model configuration
    model_config = ConfigDict(extra="allow")


class YoutubePlaylist(BaseModel):
    channel_url: str
    channel_id: str
    channel: str
    availability: str

    entries: List[YoutubeVideo]

    # Using ConfigDict to set model configuration
    model_config = ConfigDict(extra="allow")


class PlaylistEntry(BaseModel):
    title: str

    # Using ConfigDict to set model configuration
    model_config = ConfigDict(extra="allow")


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


class YoutubeToolError(Exception):
    """Custom exception for YoutubeTool-related errors."""

    pass
