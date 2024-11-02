from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor
from enum import Enum
from youtube_tool import YoutubePlaylist, YoutubeToolError


class PlaylistAction(Enum):
    REMOVE = "ACTION_REMOVE_VIDEO_BY_VIDEO_ID"
    # Add more actions as needed


class Playlist:
    def __init__(self, playlist_id: str, api_session: YoutubeBaseInfoExtractor):
        self.playlist_id = playlist_id  # "WL"
        self.api_session = api_session

    def fetch_playlist(self) -> YoutubePlaylist:
        api = self.api_session

        if not api.is_authenticated:
            raise YoutubeToolError("Not authenticated")

        # response = api.
        raise NotImplementedError

    def add_video_to_playlist(self, video_id: str, playlist_id: str):
        raise NotImplementedError

    def remove_video(self, video_id: str):
        action = {
            "removedVideoId": video_id,
            "action": PlaylistAction.REMOVE,
            # "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
        }
        endpoint = "browse/edit_playlist?prettyPrint=false"
        query = {
            "actions": [action],
            "playlistId": self.playlist_id,
            "params": "CAFAAQ%3D%3D",
        }
        response = self.api_session._extract_response(
            ep=endpoint,
            query=query,
            item_id=video_id,
            note=f"Removing video from {self.playlist_id} playlist",
            # video_id=video_id,
        )
        return response
