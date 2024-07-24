from requests import Session
from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

class YoutubeTool:
    def __init__(self, ydl: YoutubeDL):
        self.ydl = ydl
        self.extractor = YoutubeBaseInfoExtractor(ydl)

    def api(self) -> Session:
        session = Session()
        session.cookies = self.ydl.cookiejar
        return session

    def fetch_data(self, url: str) -> dict:
        return self.ydl.extract_info(url, download=False)

    def get_playlist(self, playlist_id: str):
        url = f"https://www.youtube.com/watch?v={playlist_id}"
        return self.fetch_data(url)
