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


def test_youtube_tool_fetch_info():
    from . import YoutubeTool
    import json

    tool = YoutubeTool("brave")
    info = tool.fetch_info("https://www.youtube.com/watch?v=amXz5QsRG-4")

    with open("info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4)
    print(info)
