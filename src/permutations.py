def permutations(arr, k):
    perm_arr = []
    used = set()
    permute(arr, k, perm_arr, used)


def permute(arr, k, perm_arr, used):
    if len(perm_arr) == k:
        print(perm_arr)
        return

    prev_elmt = None
    for i, elmt in enumerate(arr):
        if i in used or elmt == prev_elmt:
            continue
        perm_arr.append(elmt)
        used.add(i)
        permute(arr, k, perm_arr, used)
        used.remove(i)
        del perm_arr[-1]
        prev_elmt = elmt


# permutations([1, 2, 3, 4], 4)
# permutations([1, 2, 2, 4], 4)
# permutations([1, 2, 3, 4], 3)
permutations([1, 2, 2, 4], 3)
