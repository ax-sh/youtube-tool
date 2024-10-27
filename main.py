from youtube_tool import YoutubeTool

yt = YoutubeTool("firefox")
# yt.remove_video_from_playlist('')
url = "https://www.youtube.com/playlist?list=WL"
wl = yt.fetch_videos_from_playlist(url)
wl
