from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
try:
    yd = yt.streams.get_highest_resolution()
    yd.download('./ytDownloads')
except KeyError:
    yt.download('./ytDownloads')
