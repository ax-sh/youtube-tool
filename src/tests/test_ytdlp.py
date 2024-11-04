import pytest
from yt_dlp import YoutubeDL

from pprint import pprint, pformat
from snapshottest import Snapshot
from pydantic import BaseModel
# # Set up options with proxy configuration
# ydl_opts = {
#     "nocheckcertificate": True,
#     "proxy": "https://localhost:8080",  # mitm proxy
#     "skip_download": True,
#     "extract_flat": "in_playlist",
#     "prefer_insecure": True,
#     "clean_infojson": True,
#     "lazy_playlist": True,
#     "no_warnings": True,
#     # "client_certificate":"~/.mitmproxy/mitmproxy-ca-cert.pem"
# }


@pytest.fixture
def ydl_opts():
    """Common options for yt-dlp."""
    return {
        "nocheckcertificate": True,
        "proxy": "https://localhost:8080",  # mitm proxy
        "skip_download": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "extractor_args": {
            "youtubetab": {"approximate_date": [""]},
            # "youtube": {  # Specific to the YouTube extractor
            #     "description": True,  # We’re interested in extracting descriptions
            # },
        },
        # "quiet": True,  # Suppress unnecessary logs
        "lazy_playlist": True,
        "clean_infojson": True,
    }


@pytest.fixture(scope="function", autouse=True)
def cleanup():
    """Fixture to clean up the output file after each test."""
    yield
    # if os.path.exists(OUTPUT_FILE):
    #     os.remove(OUTPUT_FILE)

class VideoDTO(BaseModel):
    id: str
    title: str
def playlist_dto(data):
    entries = data["entries"]
    dto = []
    for entry in entries:
        dto.append(VideoDTO(**entry))
    return dto


@pytest.mark.usefixtures("snapshot")
def test_youtube_scrape_playlist(ydl_opts, snapshot: Snapshot):
    print(ydl_opts, "ddd")
    """Test if yt-dlp can download a specific format (e.g., audio only)."""
    audio_opts = ydl_opts.copy()
    playlist_url = (
        "https://www.youtube.com/playlist?list=PLffJUy1BnWj13MxDDbXWcbPzna0UESH59"
        # "https://www.youtube.com/watch?v=8IWV6I1mK6U&list=PLIGDNOJWiL1-zscX224pibRBb4RChTpgM"
    )

    with YoutubeDL(audio_opts) as ydl:
        data = ydl.extract_info(playlist_url)
        # Exclude or mask the dynamic field
    data["epoch"] = "<ignored>"
    data["thumbnails"] = "<ignored>"
    snapshot.assert_match(data, "playlist")
    entries = playlist_dto(data)
    pprint(entries)
    # snapshot.assert_match(data['entries'], "playlist_videos")
