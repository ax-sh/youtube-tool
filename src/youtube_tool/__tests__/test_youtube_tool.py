from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

from ...youtube_tool import CookiesBrowsers, YoutubeTool
from pprint import pprint, pformat

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
    api = tool.api()
    video_id = "STUL431Urfk"
    # c =  tool.extractor._download_ytcfg('web', 'STUL431Urfk')
    # o = tool.extractor.extract_yt_initial_data()
    action = {
        "removedVideoId": video_id,
        "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
    }
    o = tool.extractor._call_api(
        "browse/edit_playlist?prettyPrint=false",
        {
            "actions": [action],
            "playlistId": "WL",
            "params": "CAFAAQ%3D%3D",
        },
        video_id,
    )
    pprint(o)
