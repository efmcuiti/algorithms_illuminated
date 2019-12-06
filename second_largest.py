import math, sys

"""
Created on: December 5th, 2019
Author: efmcuiti [efmcuiti@gmail.com]
"""

def second_largest(array):
    '''
    array: Array of unsorted numbers (length power of 2).

    return the second largest number within the array.
    '''
    assert 2**(int(math.log2(len(array)))) is len(array)

    unsorted = array[:]

    def reduce_array(bigGuy):
        '''
        bigGuy: array with unsorted numbers.

        return mutated array without biggest and lowest values.
        '''
        g, l = 0, sys.maxsize
        for i in bigGuy:
            if  i > g:
                g = i
            elif i < l:
                l = i
        bigGuy.remove(g)
        bigGuy.remove(l)
    reduce_array(unsorted)

    return findBiggest(unsorted)

def findBiggest(array):
    '''
    array: set with unsorted numbers.

    return the biggest number in an array.
    '''
    if len(array) is 1:
        return array[0]
    else:
        mid = len(array) // 2
        left, right = findBiggest(array[:mid]), findBiggest(array[mid:])
        return left if left > right else right
