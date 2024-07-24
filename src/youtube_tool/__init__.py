from requests import Session
from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

from src.youtube_tool.types import CookiesBrowsers


class YoutubeTool:
    def __init__(self, client: YoutubeDL | CookiesBrowsers) -> None:
        self.ydl = (
            YoutubeDL(self.make_youtube_dl_config(client))
            if isinstance(client, str)
            else client
        )
        self.extractor = YoutubeBaseInfoExtractor(self.ydl)
        # cookies = [i for i in self.ydl.cookiejar if i.domain == ".youtube.com"]

    @staticmethod
    def make_youtube_dl_config(browser: str):
        options = {
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
        if browser:
            options.update({"cookiesfrombrowser": (browser,)})

        return options

    def api(self) -> Session:
        session = Session()
        session.cookies = self.ydl.cookiejar
        return session

    def fetch_info(self, url: str) -> dict:
        return self.ydl.extract_info(url, download=False)

    def get_playlist(self, playlist_id: str):
        url = f"https://www.youtube.com/watch?v={playlist_id}"
        return self.fetch_info(url)
