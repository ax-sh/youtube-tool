from requests import Session
from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

from bs4 import BeautifulSoup as Soup
from typing_extensions import TypedDict

from .constants import WATCH_LATER_URL
from .types import CookiesBrowsers, VideoInfo, PlaylistEntry, YoutubePlaylist


class YtcfgDict(TypedDict, total=False):
    VISITOR_DATA: str


class YoutubeTool:
    OPTIONS = {
        "extract_flat": "in_playlist",
        "dump_single_json": True,
        "allow_unplayable_formats": True,
        "ignoreerrors": False,
        "no_warnings": True,
        "clean_infojson": True,
        "lazy_playlist": True,
        # 'logger': YoutubeUtilsLogger(),
        # extractor_args E.g. {'youtube': {'skip': ['dash', 'hls']}}
        "extractor_args": {"youtubetab": {"approximate_date": [""]}},
    }

    def __init__(self, client: YoutubeDL | CookiesBrowsers) -> None:
        self.ydl = (
            YoutubeDL(self.make_youtube_dl_config(client))
            if isinstance(client, str)
            else client
        )
        self.extractor = YoutubeBaseInfoExtractor(self.ydl)
        # cookies = [i for i in self.ydl.cookiejar if i.domain == ".youtube.com"]

    @classmethod
    def make_youtube_dl_config(cls, browser: str):
        options = {"cookiesfrombrowser": (browser,)}

        if browser:
            options.update(cls.OPTIONS)

        return options

    def _api(self) -> Session:
        session = Session()
        session.cookies = self.ydl.cookiejar
        return session

    def fetch_info(self, url: str) -> dict:
        return self.ydl.extract_info(url, download=False)

    def get_playlist(self, playlist_id: str):
        url = f"https://www.youtube.com/watch?v={playlist_id}"
        return self.fetch_info(url)

    @staticmethod
    def parse_playlist(info: dict) -> YoutubePlaylist:
        return YoutubePlaylist(**info)

    def find_ytcfg_from_yt_dlp(self, soup: Soup, video_id: str) -> YtcfgDict:
        webpage = soup.text
        return self.extractor.extract_ytcfg(video_id, webpage)

    def remove_video_from_playlist(self, video_id: str):
        action = {
            "removedVideoId": video_id,
            "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
        }
        endpoint = "browse/edit_playlist?prettyPrint=false"
        query = {
            "actions": [action],
            "playlistId": "WL",
            "params": "CAFAAQ%3D%3D",
        }
        response = self.extractor._extract_response(
            ep=endpoint,
            query=query,
            item_id=video_id,
            # video_id=video_id,
        )
        return response

    def fetch_videos_from_playlist(self, url: str) -> YoutubePlaylist:
        info = self.fetch_info(url)
        return YoutubePlaylist(**info)

    def fetch_videos_from_watchlist(self) -> YoutubePlaylist:
        return self.fetch_videos_from_playlist(WATCH_LATER_URL)
