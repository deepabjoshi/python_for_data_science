"""
Read two directories, compare files, based on user input move files or discard files as required.
Use following modules:
pathlib, sys, glob - for finding
re - for finding and renaming files
shutil - for moving or copying files. It might make sense to copy a small part of new dir first

"""
from pathlib import Path
import argparse
import shutil
import sys
from collections import defaultdict


def get_dir_data(dir):
    files = {}
    sub_dirs = {}
    for path in dir.glob('*'):
        if path.is_dir():
            sub_dirs[path.name] = path
        else:
            files[path.name] = path.stat()
    return files, sub_dirs


def get_dir_data_recursive(dir):
    files = []
    try:
        files = defaultdict(list)
        for path in dir.rglob('*'):
            if path.is_dir():
                continue
            files[path.name].append((path.parent, path.stat().st_size))
    except Exception as e:
        print("Something went wrong while reading directory: ", e, file=sys.stderr)
    return files


def compare_files(new_dir_files, prev_dir_files):
    new_files = {}
    mismatched_files = {}
    duplicate_files = {}
    for f in new_dir_files:
        if f in prev_dir_files:
            if new_dir_files[f].st_size == prev_dir_files[f].st_size:
                duplicate_files[f] = [f]
            else:
                mismatched_files[f] = [f, 'New size:', new_dir_files[f].st_size,
                                       'Old size:', prev_dir_files[f].st_size]
        else:
            new_files[f] = [f]
    return new_files, mismatched_files, duplicate_files


def move_duplicates(newdir, movedir, duplicate_files):
    dest_dir = movedir.joinpath(*newdir.parts[1:])
    print('MOVING TO:', dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    for f in duplicate_files.keys():
        # print(newdir / f, dest_dir / f)
        shutil.move(newdir / f, dest_dir / f)
    for f in newdir.iterdir():
        print('DIR NOT EMPTY:', newdir)
        break
    else:
        print('REMOVING DIR:', newdir)
        newdir.rmdir()


def print_report(new_files, mismatched_files, duplicate_files):
    for f in new_files:
        print('NEW:', *new_files[f])
    for f in mismatched_files:
        print('MISMATCH:', *mismatched_files[f])
    for f in duplicate_files:
        print('DUPLICATE:', *duplicate_files[f])


def compare_directories(newdir, prevdir, movedir=None, verbose=False):
    prev_dir_files, prev_sub_dirs = get_dir_data(prevdir)
    new_dir_files, new_sub_dirs = get_dir_data(newdir)
    for d in new_sub_dirs:
        if d in prev_sub_dirs:
            compare_directories(new_sub_dirs[d], prev_sub_dirs[d], movedir)
        else:
            print('New subdir:', new_sub_dirs[d])

    new_files, mismatched_files, duplicate_files = compare_files(new_dir_files, prev_dir_files)
    print('\nCOMPARING:', newdir, prevdir)
    print('N M D:', len(new_files), len(mismatched_files), len(duplicate_files))

    if verbose:
        print_report(new_files, mismatched_files, duplicate_files)

    if movedir:
        move_duplicates(newdir, movedir, duplicate_files)


def find_duplicates(newdir, backupdir, movedir=None, verbose=False):
    new_files = {}
    mismatched_files = {}
    duplicate_files = {}
    backup_files = get_dir_data_recursive(backupdir)
    for path in newdir.glob('*'):
        if path.is_dir():
            find_duplicates(path, backupdir, movedir, verbose)
            continue
        if path.name in backup_files:
            new_file_size = path.stat().st_size
            mismatch = []
            for f, size in backup_files[path.name]:
                if new_file_size == size:
                    duplicate_files[path.name] = [path.name, path.parent, f]
                    break
                else:
                    mismatch.append((f, size))
            else:
                mismatched_files[path.name] = [path.name, new_file_size, *mismatch]
        else:
            new_files[path.name] = [path.name, path.parent]

    print('\nFINDING DUPLICATES IN:', newdir)
    print('N M D:', len(new_files), len(mismatched_files), len(duplicate_files))
    if verbose:
        print_report(new_files, mismatched_files, duplicate_files)

    if movedir:
        move_duplicates(newdir, movedir, duplicate_files)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('newdir',
                        help='New directory that will be compared against a previous directory')
    parser.add_argument('prevdir',
                        help='Existing directory with which the new directory will be compared')
    parser.add_argument('-v', '--verbose', help='Print all details of comparison',
                        action='store_true')
    parser.add_argument('--cmp', help='Compare the two directories', action='store_true')
    parser.add_argument('--find', help="Find files from new directory in existing directory",
                        action='store_true')
    parser.add_argument('--movedir', help='Directory where files from new directory will be moved')
    args = parser.parse_args()

    print(args)
    move_path = None
    if args.movedir:
        move_path = Path(args.movedir)

    if args.cmp:
        compare_directories(Path(args.newdir), Path(args.prevdir), move_path, args.verbose)
    elif args.find:
        find_duplicates(Path(args.newdir), Path(args.prevdir), move_path, args.verbose)


if __name__ == '__main__':
    main()

