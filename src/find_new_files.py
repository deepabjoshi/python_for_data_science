"""
Find examples of argparse and pathlib here.
Given a directory and a list of backup directories, find the files in new directory which are not
present in the backup directories. It can accept a list of extensions as well and look only for
those extensions. If no extension is provided, all files are examined. If a file with the same name
is found in any backup directory, then the sizes of the file are compared. If sizes do not match, a
message displaying file name and sizes is displayed.
"""

import argparse
from pathlib import Path


def check_extension(name, ext_list):
    if not ext_list:
        return True
    for ext in ext_list:
        if name.endswith(ext):
            return True
    return False


def get_backup_file_info(backup_dirs, ext_list):
    backup_file_info = {}
    for backup_dir in backup_dirs:
        for path in Path(backup_dir).rglob("*"):
            if not check_extension(path.name, ext_list):
                continue
            if path.is_file():
                if path.name not in backup_file_info:
                    backup_file_info[path.name] = []
                backup_file_info[path.name].append([str(path), path.stat().st_size])
                # print(path.name, backup_file_info[path.name])
    return backup_file_info


def check_new_files(new_dirs, backup_file_info, verbose, ext_list, debug_level=0):
    print('debug_level =', debug_level)
    for new_dir in new_dirs:
        # Example: reading a directory
        for path in Path(new_dir).rglob("*"):
            # Example: check if file or directory. Could have also used path.is_dir()
            if not path.is_file():
                continue
            if not check_extension(path.name, ext_list):
                continue
            if path.name not in backup_file_info:
                print("NEW:", path.parent, path.name)
            else:
                # Example:  get path stats to check size. samefile() is also interesting
                size = path.stat().st_size
                for f in backup_file_info[path.name]:
                    if size != f[1] and debug_level > 0:
                        print("MISMATCH:", path.parent, path.name, size > f[1], size, f[0], f[1])
                    elif verbose or debug_level > 1:
                        print("EXISTS:", path.parent, path.name, f[0])


def main():
    parser = argparse.ArgumentParser()
    # Example: argparse positional arguments
    parser.add_argument("newdirlist",
                        help="comma separated list of new directories that need to be examined")
    parser.add_argument("backupdirlist", help="comma separated list of backup directories")
    # Example: argparse optional argument which does not need any value
    parser.add_argument("-v", "--verbose", help="print all details of comparison",
                        action="store_true")
    # Example: argparse optional argument which needs a value
    parser.add_argument("--extlist", help="comma separated list of extensions to be examined")
    # Example: argparse otpional argument which needs a set of values
    parser.add_argument("--debug", help="increase debug level", type=int,
                        choices=[0, 1, 2], default=0)
    args = parser.parse_args()

    ext_list = None
    if args.extlist:
        ext_list = args.extlist.split(',')

    backup_dirs = args.backupdirlist.split(',')
    backup_file_info = get_backup_file_info(backup_dirs, ext_list)

    new_dirs = args.newdirlist.split(',')

    check_new_files(new_dirs, backup_file_info, args.verbose, ext_list, args.debug)


if __name__ == '__main__':
    main()
