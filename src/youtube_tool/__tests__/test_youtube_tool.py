from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

from ..parser import JsonPath
from ...youtube_tool import CookiesBrowsers, YoutubeTool, YoutubePlaylist
from pprint import pprint, pformat
from pydantic import ValidationError

BROWSER: CookiesBrowsers = "vivaldi"


def test_number_one():
    """Docstring"""
    assert 1 == 1


def test_youtube_tool_init_browser():
    tool = YoutubeTool(BROWSER)

    # assert tool.extractor._cookies_passed == True
    assert tool.extractor.is_authenticated


def test_youtube_dl_cookiesfrombrowser():
    browser = "vivaldi"
    # browser = "brave"
    ydl = YoutubeDL(
        {
            "cookiesfrombrowser": (browser,),
        }
    )
    extractor = YoutubeBaseInfoExtractor(ydl)
    # print(extractor.cookiejar)
    assert extractor.is_authenticated


def test_youtube_tool_fetch_info():
    tool = YoutubeTool(BROWSER)
    parsed = tool.fetch_videos_from_playlist(
        "https://www.youtube.com/watch?v=&list=PLQQsYaXd5huAqbx5q1cZvHqYRhV3Gv56s"
    )
    pprint(parsed.entries)
    entry = parsed.entries[0]
    pprint(entry.thumbnails)
    print(entry.thumb)


def test_youtube_tool_remove_video_from_playlist():
    tool = YoutubeTool(BROWSER)
    video_id = "STUL431Urfk"
    removed_result = tool.remove_video_from_playlist(video_id)
    # c =  tool.extractor._download_ytcfg('web', 'STUL431Urfk')
    # o = tool.extractor.extract_yt_initial_data()

    print(removed_result["status"])


def test_youtube_tool_parse_watchlater_playlist():
    path = JsonPath[dict](__file__).parent
    data = path.joinpath("wl.json").read_json()
    try:
        parsed = YoutubePlaylist(**data)
        print(parsed)
    except ValidationError as e:
        for i in e.errors():
            print(i)
            break
        # pprint(len(e.errors()))


def test_youtube_tool_fetch_watchlater_playlist():
    tool = YoutubeTool(BROWSER)
    # parsed = tool.fetch_info("https://www.youtube.com/playlist?list=WL")
    # # JsonPath[dict]('wl.json').write_json(parsed)
    # print(parsed)


def test_youtube_tool_parse_watchlater_playlist_to_json():
    import sqlite3
    import pandas as pd
    import json

    path = JsonPath[dict](__file__).parent
    data = path.joinpath("wl.json").read_json()
    entries = json.loads(YoutubePlaylist(**data).model_dump_json())
    df = pd.DataFrame(entries["entries"])
    df = df.drop("thumbnails", axis=1)
    conn = sqlite3.connect(path / "watch_later.db")
    df.to_sql("watch_later_table", conn, if_exists="replace")
    df.to_csv(path / "watch_later.csv")
    (path / "watch-later.json").write_json(entries)
    # df.to_csv("dd.csv", index=False)
    # print(df)
