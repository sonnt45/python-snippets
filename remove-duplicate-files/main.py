import hashlib
from pathlib import Path
from typing import List

FILE_READING_BLOCK_SIZE = 65536


def hash_file(path: Path) -> str:
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        buffer = file.read(FILE_READING_BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(FILE_READING_BLOCK_SIZE)

    return hasher.hexdigest()


def get_duplicate_file_list(path: Path) -> List[Path] | None:
    if not path.exists():
        print(f'Path {path} does not exist.')
        return None

    digest_map = {}
    duplicate_files = []
    for item in path.iterdir():
        if item.is_file():
            digest = hash_file(item)
            if digest in digest_map:
                duplicate_files.append(item)
            else:
                digest_map[digest] = item

    return duplicate_files


def delete_files(paths: List[Path]):
    for file in paths:
        file.unlink()
        print(f'Deleted file {file.name}.')

        parent_dir = file.parent
        if not any(parent_dir.iterdir()):
            parent_dir.rmdir()
            print(f'Deleted directory {parent_dir.name}.')


def main():
    duplicate_files = get_duplicate_file_list(Path('path-to-somewhere'))
    if len(duplicate_files) > 0:
        delete_files(duplicate_files)


main()
