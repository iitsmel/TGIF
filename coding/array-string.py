#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

import random
from functools import singledispatch

@singledispatch
def checkInteger(nums1, m, nums2, n):
    maximum = 10_000_000
    minimum = -10_000_000
    total = list(nums1) + list(nums2) + [m,n]
    for value in total:
        turn_string = str(value)
        if not turn_string.lstrip('-+').isdigit():
            return False
        if value >= maximum or minimum >= value:
            return False
    return True

# https://leetcode.com/problems/merge-sorted-array/description/
# Merge Sorted Array, easy
class MergeSortedArray:
    def merge(self, nums1, m, nums2, n):
        if not checkInteger(nums1, m, nums2, n):
            return False
        
        nums1[:m+n] = sorted(nums1[:m] + nums2[:n])
        return sorted(nums1[:m] + nums2[:n])

msa_ds = MergeSortedArray()
def get_msa(_):
    print("Merge Sorted Array")
    print("happy path")
    print(msa_ds.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(msa_ds.merge([1], 1, [], 0))
    print(msa_ds.merge([0], 0, [1], 1))
    print(msa_ds.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
    print(msa_ds.merge([2,4,6,0,0,0], 3, [1,3,5], 3))
    print(msa_ds.merge([5,7,9,0,0], 3, [6,8], 2))
    print(msa_ds.merge([3,5,7,10,0,0,0], 4, [1,2,8], 3))
    print(msa_ds.merge([1,1,3,0,0,0], 3, [1,2,4], 3))
    print(msa_ds.merge([10,20,30,0,0,0], 3, [15,25,35], 3))

    print()

    print("monkey test")
    print(msa_ds.merge([100,200,300,0,0,0], 3, [150,250,350], 3))
    print(msa_ds.merge([500,600,700,0,0,0,0], 3, [100,800,900,1000], 4))
    print(msa_ds.merge([100000,0], 1, [99999], 1))
    print(msa_ds.merge([0,0,0,0,0], 0, [50000,100000,150000,200000,250000], 5))
    print(msa_ds.merge([12345,54321,0,0], 2, [33333,44444], 2))

    print()

    print("corner case")
    print(msa_ds.merge([0,0,0,0], 0, [1,2,3,4], 4))
    print(msa_ds.merge([5,0], 1, [5], 1))
    print(msa_ds.merge([-2,0], 1, [-3], 1))
    print(msa_ds.merge([0], 0, [0], 1))
    print(msa_ds.merge([1,1,1,0,0], 3, [1,1], 2))
    print(msa_ds.merge([3,4,5,0,0,0], 3, [-1,-2,-3], 3))
    print(msa_ds.merge([1000000000,0], 1, [-1000000000], 1))
    print(msa_ds.merge([0,0,0], 0, [0,0,0], 3))
    print(msa_ds.merge([1,2,3], 3, [], 0))
    print(msa_ds.merge([0,0,0], 0, [], 0))
    
    print()

    print("edge case")
    edges = [
        # TypeError: wrong type
        ([-1.1, -2.2, -3.3], 1, [2], 2), # float in list
        (['hello', -2.2, -3.3], 1, [2], 2), # string/float in list
        ([{1:'hello'}], 1, [2], 2), # dict in list
        (1 ,1, [2], 2), # int not list
        (1 ,1, [[2]], 2), # int not list, nested list
        ([{1:'hello'}], [{1:'hello'}], [{1:'hello'}], [{1:'hello'}]), # dict in list, all wrong type
        ([2], [2], [2], [2], [2]), # too many arguments
        ([0,0,0],'print(msa_ds.merge([2,4,6,0,0,0], 3, [1,3,5], 3))', [2], 2), # string not int

        # TypeError: missing argument
        (1, [2], 2), # missing one argument
        (), # missing all arguments

        # ValueError: out of range
       ([2000000000,4,6,0,0,0], 3, [1,3,5], 3), # too big
       ([-2000000000,4,6,0,0,0], 3, [1,3,5], 3), # too small
    ]

    """
       # Python evaluates test cases before function call, pass arguments as strings to solve the errors
       # ValueError/OverflowError: impossible to calculate
        ([0,0,0],1, [2], 10 ** (-10 ** 10)), # impossible negative integer
        ([0,10 ** (-10 ** 10),0],1, [2], 1), # impossible negative integer in list
        ([0,0,0],1, [10 ** (10 ** 10)], 4), # impossible integer in list

        # SyntaxError: invalid syntax
        ({-1.1: -2.2, -'hello': -3.3}, 1, [2], 2), # invalid dict key: -'hello'
    """

    for eCases in edges:
        try:
            print(msa_ds.merge(*eCases))
        except Exception:
            print("Error:", eCases)

get_msa(None)


print()

if input("Next: Remove Duplicates from Sorted Array \ncontinue: ").strip().lower() != "y":
    exit()

print()


