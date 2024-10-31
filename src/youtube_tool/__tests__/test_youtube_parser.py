import pytest

from typing import TypedDict, List

from pydantic import ValidationError

from ..parser import JsonPath
from ..types import VideoInfo


class Entry(TypedDict):
    uploader: str


class PlaylistData(TypedDict):
    entries: List[Entry]
    title: str


@pytest.mark.skip(reason="This test is not ready yet.")
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


def test_video_info_validation():
    # Example dictionary
    data = {
        "description": None,
        "uploader": "Supabase",
        "uploader_id": "@Supabase",
        "uploader_url": "https://www.youtube.com/@Supabase",
        "release_timestamp": None,
        "availability": None,
        "live_status": None,
        "channel_is_verified": None,
        "__x_forwarded_for_ip": None,
    }

    # Validate data using the Pydantic model
    try:
        video_info = VideoInfo(**data)
    except ValidationError as e:
        pytest.fail(f"Validation error: {e}")
