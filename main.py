from youtube_tool import YoutubeTool
from pathlib import Path
import json


def fetch_watchlater():
    yt = YoutubeTool("vivaldi")
    # yt.remove_video_from_playlist('')
    # url = "https://www.youtube.com/playlist?list=WL"
    wl = yt.fetch_videos_from_watchlist()

    return wl


wl = fetch_watchlater()
path = Path(__file__).parent.absolute()
data = path / "watchlist.json"
with data.open("w", encoding="utf-8") as f:
    json.dump(wl, f, indent=4)
