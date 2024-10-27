from youtube_tool import YoutubeTool

def main():
    yt = YoutubeTool("vivaldi")
    # yt.remove_video_from_playlist('')
    # url = "https://www.youtube.com/playlist?list=WL"
    wl = yt.fetch_videos_from_watchlist()
    print(wl)

main()