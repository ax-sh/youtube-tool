from typing import Literal, Optional, List
from pydantic import BaseModel, HttpUrl

CookiesBrowsers = Literal["brave", "chrome", "vivaldi", "firefox", ""]


class YoutubeVideo(BaseModel):
    id: str
    url: str
    title: str
    view_count: int
    duration: int
    # thumbnails:

    class Config:
        extra = "allow"


class YoutubePlaylist(BaseModel):
    channel_url:str
    channel_id:str
    channel:str
    availability:str

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
