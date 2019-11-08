"""
Created on: November 7, 2019
Author: efmcuiti
"""
def mergeSort(l):
    """
    l: A list of number (or anything comparable).

    Return the same list but ordered.
    """
    assert type(l) is list

    if not l or len(l) is 1:
        return l
    else:
        half = len(l) // 2
        lh, rh = mergeSort(l[:half]), mergeSort(l[half:])
        return merge(lh, rh)

def merge(l1, l2):
    """
    l1, l2: Lists of integers (might be empty). Arrays are assumed to be sorted.

    Returns the lists merged.
    """
    n = len(l1) + len(l2)
    merged = []
    i, j, = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    complement = [e for e in l1[i:]] if i < len(l1) else [e for e in l2[j:]]

    assert len(complement) + len(merged) is n

    return merged + complement

