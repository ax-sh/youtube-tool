from pathlib import Path
import json
from typing import TypeVar, Generic, TypedDict


T = TypeVar("T", bound=TypedDict)


class JsonPath(Path, Generic[T]):
    def read_json(self) -> T:
        with self.open("r",encoding='utf-8') as f:
            return json.load(f)

    def write_json(self, data: T, indent: int = 4) -> None:
        with self.open("w",encoding='utf-8') as f:
            json.dump(data, f, indent=indent)


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
