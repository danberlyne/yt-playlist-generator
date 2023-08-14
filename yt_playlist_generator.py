#!/usr/bin/env python3
# yt_playlist_generator.py - Creates a YouTube playlist from a list of URLs.

def main():
    file = open('urls.txt')
    urls = [line.strip() for line in file.readlines()]
    file.close()
    ids = [url[-11:] for url in urls]
    playlist = 'https://www.youtube.com/watch_videos?video_ids=' + ','.join(ids)
    print(f'Playlist created at: {playlist}')

if __name__ == '__main__':
    main()