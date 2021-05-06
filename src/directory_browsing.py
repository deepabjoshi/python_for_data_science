"""
See examples of reading directories recursively and finding files within a
directory.
This script takes various paths and looks for photos with given extensions.
It compares two directories and finds files that are present only in first,
second and in both directories. It also checks if file sizes are same for
the common files.
"""
import glob
import os

BACKUP2_PHOTOS_PATH = ['/media/deepa/backup2/backup2-nov2018/deepa-1-pictures/',
                       '/media/deepa/backup2/backup2-nov2018/memories/pictures/'
                       ]
BACKUP2_PHOTOS_EXTENSION = ['jpg', 'JPG', 'png', 'PNG', 'MOV', 'mp4', 'mp3',
'wav', 'WAV']
COMPARE_THRESHOLD = 0


def find_pairs(dir_list, pairs_dict):
    sorted_dir_list = sorted(dir_list)
    for i in range(0, len(sorted_dir_list)):
        for j in range(i + 1, len(sorted_dir_list)):
            pair = (sorted_dir_list[i], sorted_dir_list[j])
            if pair not in pairs_dict:
                pairs_dict[pair] = 0
            pairs_dict[pair] += 1


def get_photo_locations(photo_paths, photo_extensions):
    photo_locations = {}
    for ph_path in photo_paths:
        for ph_ext in photo_extensions:
            # print("DEEPA1: ", ph_path, ph_ext)
            for filename in glob.iglob(ph_path + '**/*.' + ph_ext, recursive=True):
                pp, pn = os.path.split(filename)
                # print("DEEPA: ", pn, pp)
                if pn in photo_locations:
                    photo_locations[pn].append(pp)
                else:
                    photo_locations[pn] = [pp]
    return photo_locations


def get_photo_stats(photo_locations):
    photo_stats = {}
    duplicate_photo_dirs = {}
    for pn in photo_locations:
        l = len(photo_locations[pn])
        if l > 1:
            find_pairs(photo_locations[pn], duplicate_photo_dirs)
            # print(pn, photo_locations[pn])
            if l not in photo_stats:
                photo_stats[l] = 0
            photo_stats[l] += 1
    return photo_stats, duplicate_photo_dirs


def compare_directories(dir_a, dir_b):
    common_files = {}
    dir_a_files = {}
    for f in os.listdir(dir_a):
        if os.path.isfile(os.path.join(dir_a, f)): dir_a_files[f] = 1

    dir_b_files = {}
    for f in os.listdir(dir_b):
        fb = os.path.join(dir_b, f)
        if not os.path.isfile(fb): continue
        if f in dir_a_files:
            fa = os.path.join(dir_a, f)
            print("DEEPA2: fa", fa, os.stat(fa).st_size)
            print("DEEPA2: fb", fb, os.stat(fb).st_size)
            if os.stat(fb).st_size == os.stat(fa).st_size:
                common_files[f] = 1
                del dir_a_files[f]
            else:
                dir_b_files[f] = 1
        else:
            dir_b_files[f] = 1

    return dir_a_files, dir_b_files, common_files


photo_locations = get_photo_locations(BACKUP2_PHOTOS_PATH, BACKUP2_PHOTOS_EXTENSION)
photo_stats, duplicate_photo_dirs = get_photo_stats(photo_locations)

photo_dir_comparison = {}
for p, v in sorted(duplicate_photo_dirs.items(), key=lambda item: item[1]):
    if v < COMPARE_THRESHOLD:
        continue
    only_in_a, only_in_b, in_both = compare_directories(p[0], p[1])
    photo_dir_comparison[p] = [only_in_a, only_in_b, in_both]
    print(p, photo_dir_comparison[p])

for p, v in sorted(photo_dir_comparison.items(),
                   key=lambda item: item[0][0] + item[0][1], #len(item[1][2].keys()),
                   reverse=True):
    num_a_only, num_b_only, num_in_both = len(v[0].keys()), len(v[1].keys()), \
                                          len(v[2].keys())
    print(num_a_only, num_b_only, num_in_both)
    if num_in_both == 0: continue
    print('INFO: ', [num_a_only, num_b_only, num_in_both], p)
    for p in sorted(v[2].keys()):
        print(p)

# for l in photo_stats:
#     print(l, photo_stats[l])
# find_pairs(['a', 'b', 'c'], duplicate_photo_dir)
# find_pairs(['a', 'b', 'pd'], duplicate_photo_dir)
# print(duplicate_photo_dir)
# for k, v in sorted(duplicate_photo_dirs.items(), key=lambda item: item[1]):
#     print(v, k)
