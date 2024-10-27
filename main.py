from youtube_tool import YoutubeTool
from pathlib import Path
import json


def fetch_watchlater():
    yt = YoutubeTool("safari")
    # yt.remove_video_from_playlist('')
    # url = "https://www.youtube.com/playlist?list=WL"
    wl = yt.fetch_videos_from_watchlist()

    return wl


wl = fetch_watchlater()
path = Path(__file__).parent.absolute()
data = path / "watchlist.json"

# print(wl.model_dump(mode="json"))
data.write_text(wl.model_dump_json())
print("DONE")
