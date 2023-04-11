import validators
from pytube import YouTube
import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def download_song(link, user_id, mp4=False):
    try:
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        if yt:
            if not mp4:
                status = yt.download(f'Downloads/{user_id}')
                video = VideoFileClip(status)
                video.audio.write_audiofile(status[:-4] + ".mp3")
                video.close()
                os.remove(status)
                status = status[:-4] + ".mp3"
                return status
            else:
                status = yt.download(f'Downloads/{user_id}')
                return status
        else:
            return -1
    except Exception:
        return -1
