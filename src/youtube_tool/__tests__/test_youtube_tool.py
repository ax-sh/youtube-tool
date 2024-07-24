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
