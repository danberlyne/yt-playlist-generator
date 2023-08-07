#!/usr/bin/env python3
# yt_playlist_generator.py - Creates a YouTube playlist from a list of URLs.

file = open('urls.txt')
urls = [line.strip() for line in file.readlines()]
file.close()
ids = [url[-11:] for url in urls]
playlist = 'https://www.youtube.com/watch_videos?video_ids=' + ','.join(ids)
print(f'Playlist created at: {playlist}')