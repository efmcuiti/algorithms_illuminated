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
        return (0, l)
    else:
        half = len(l) // 2
        lh, rh = mergeSort(l[:half]), mergeSort(l[half:])
        m = merge(lh[1], rh[1])
        return (lh[0] + rh[0] + m[0], m[1])

def merge(l1, l2):
    """
    l1, l2: Lists of integers (might be empty). Arrays are assumed to be sorted.

    Returns the lists merged.
    """
    n = len(l1) + len(l2)
    merged = []
    i, j, s = 0, 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
            s += (n//2)-i


    complement = [e for e in l1[i:]] if i < len(l1) else [e for e in l2[j:]]

    assert len(complement) + len(merged) is n

    return (s, merged + complement)

