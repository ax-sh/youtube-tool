import pytest

from yt_dlp import YoutubeDL
from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor

from src.youtube_tool import CookiesBrowsers

BROWSER: CookiesBrowsers = "vivaldi"


def test_number_one():
    """Docstring"""
    assert 1 == 1


def test_youtube_tool_init_browser():
    from . import YoutubeTool

    tool = YoutubeTool(BROWSER)

    # assert tool.extractor._cookies_passed == True
    assert tool.extractor.is_authenticated == True


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
    assert extractor.is_authenticated == True


def test_youtube_tool_fetch_info():
    from . import YoutubeTool
    import json

    tool = YoutubeTool(BROWSER)
    info = tool.fetch_info(
        "https://www.youtube.com/watch?v=&list=PLQQsYaXd5huAqbx5q1cZvHqYRhV3Gv56s"
    )

    with open("info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4)
    print(info)
