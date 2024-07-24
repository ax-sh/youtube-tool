from typing import TypedDict

from ..parser import JsonPath
from ..types import VideoInfo


class PlaylistData(TypedDict):
    entries: str
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
        entry = VideoInfo(**i)
        print(entry.uploader)
