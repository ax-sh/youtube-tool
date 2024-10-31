from youtube_tool import YoutubeTool, CookiesBrowsers
from pathlib import Path

browser: CookiesBrowsers = "firefox"


def fetch_watchlater():
    yt = YoutubeTool(browser)
    # yt.remove_video_from_playlist('')
    # url = "https://www.youtube.com/playlist?list=WL"
    wl = yt.fetch_videos_from_watchlist()

    return wl


print(browser, "fetching watch later playlist")
wl = fetch_watchlater()
path = Path(__file__).parent.absolute()
data = path / "watchlist.json"

# print(wl.model_dump(mode="json"))
data.write_text(wl.model_dump_json(indent=2))
print("DONE")
