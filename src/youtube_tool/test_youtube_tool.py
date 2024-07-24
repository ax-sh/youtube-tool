from pywin.framework.toolmenu import tools
from yt_dlp import YoutubeDL

BROWSER = "brave"


def test_number_one():
    """Docstring"""
    assert 1 == 1


def test_youtube_tool_init_browser():
    from . import YoutubeTool

    tool = YoutubeTool("brave")

    assert tool.extractor._cookies_passed == True

def test_youtube_tool_init_browser():
    #     from . import YoutubeTool
    #     browser = BROWSER
    #
    #     ydl =
    #
    #     tool = YoutubeTool(ydl)
    #     print(tool.api().cookies)
