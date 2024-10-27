# youtube-tool

## To use in project
```shell
pip install git+https://github.com/ax-sh/youtube-tool
# https://github.com/ax-sh/youtube-tool/tree/master

rye add youtube-tool --git=https://github.com/ax-sh/youtube-tool
```
```python
from youtube_tool import YoutubeTool
yt = YoutubeTool('chrome')
# yt.remove_video_from_playlist('')
url = 'https://www.youtube.com/playlist?list=WL'
wl = yt.fetch_videos_from_playlist(url)
wl
```



##  To run tests use
```shell
rye test -- --ruff --ruff-format -p sugar
```


## For running main 
```sh 
rye run python main.py
```