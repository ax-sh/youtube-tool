from typing import Literal, Optional
from pydantic import BaseModel, HttpUrl

CookiesBrowsers = Literal["brave", "chrome", "vivaldi", ""]


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
