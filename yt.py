from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor
import yt_dlp
from pprint import pprint

class CustomYoutubePlaylistExtractor(YoutubeBaseInfoExtractor):
    def _real_extract(self, url: str):
        print("ffff")
        # Call the parent class's _real_extract method to get the playlist data
        playlist_data = super(CustomYoutubePlaylistExtractor, self)._real_extract(url)
        playlist_entries = []

        for entry in playlist_data["entries"]:
            # Extract necessary metadata from each entry
            video_info = {
                "title": entry.get("title"),
                "id": entry.get("id"),
                "url": f"https://www.youtube.com/watch?v={entry.get('id')}",
            }
            playlist_entries.append(video_info)

        return "dooo"

        return {"title": playlist_data.get("title"), "entries": playlist_entries}


# Instantiate youtube_dl with custom extractor
class CustomYoutubeDL(yt_dlp.YoutubeDL):
    def __init__(self, params=None):
        super().__init__(params)
        # Register the custom extractor
        self.add_info_extractor(CustomYoutubePlaylistExtractor(self))


# Example usage
def fetch_playlist_data(playlist_url):
    ydl_opts = {
        # "extract_flat": True,
        "extract_flat": "in_playlist",
        "lazy_playlist": True,
        "extractor_args": {"youtubetab": {"approximate_date": [""]}},
        "quiet": True  # Suppress unnecessary logs

    }

    with CustomYoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)

    return result


# Use your playlist URL
playlist_url = "https://www.youtube.com/watch?v=KbyYTjfgZJI&list=PLffJUy1BnWj13MxDDbXWcbPzna0UESH59"
# playlist_url = ":ytwatchlater"
playlist_data = fetch_playlist_data(playlist_url)
print("Playlist Title:", playlist_data["title"])
pprint(playlist_data)
# for video in playlist_data["entries"]:
#
#     print(f"Title: {video['title']}, URL: ")
