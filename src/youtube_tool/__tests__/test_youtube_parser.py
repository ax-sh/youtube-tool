from typing import TypedDict, List

from ..parser import JsonPath
from ..types import VideoInfo


class Entry(TypedDict):
    uploader: str


class PlaylistData(TypedDict):
    entries: List[Entry]
    title: str


def test_parse_json():
    path = JsonPath(__file__).parent
    print()
    json_file: JsonPath[PlaylistData] = path.joinpath("./info_playlist.json")
    data: PlaylistData = json_file.read_json()
    entries = data["entries"]
    title = data["title"]
    print(title)
    assert len(entries) == 8
    for i in entries:
        i[""]
        entry = VideoInfo(**i)
        print(entry.uploader)
