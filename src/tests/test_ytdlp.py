import pytest
from yt_dlp import YoutubeDL

from pprint import pprint, pformat
from snapshottest import Snapshot

@pytest.fixture
def ydl_opts():
    """Common options for yt-dlp."""
    return {
        "nocheckcertificate": True,
        "proxy": "https://localhost:8080",  # mitm proxy
        "skip_download": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "lazy_playlist": True,
    }


@pytest.fixture(scope="function", autouse=True)
def cleanup():
    """Fixture to clean up the output file after each test."""
    yield
    # if os.path.exists(OUTPUT_FILE):
    #     os.remove(OUTPUT_FILE)


@pytest.mark.usefixtures("snapshot")
def test_youtube_scrape_playlist(ydl_opts, snapshot: Snapshot):
    """Test if yt-dlp can download a specific format (e.g., audio only)."""
    audio_opts = ydl_opts.copy()
    playlist_url = (
        "https://www.youtube.com/playlist?list=PLffJUy1BnWj13MxDDbXWcbPzna0UESH59"
    )

    with YoutubeDL(audio_opts) as ydl:
       data = ydl.extract_info(playlist_url)
    pprint(data)
    snapshot.assert_match(data, "user_data_snapshot")
