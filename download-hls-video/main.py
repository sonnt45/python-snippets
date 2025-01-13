import subprocess
from pathlib import Path


def download(url: str, path: Path, overwrite: bool = False):
    if path.exists() and not overwrite:
        print('Video already downloaded.')
        return

    subprocess.run([
        'streamlink',
        url,
        'best',
        '--stream-segment-threads', '4',
        '-o', path
    ], check=True)


def main():
    url = 'https://dum.my/hls/index.m3u8'
    path = Path('path-to-file.mp4')
    download(url, path)


main()
