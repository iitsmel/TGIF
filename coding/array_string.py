#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

import random
from functools import singledispatch

@singledispatch
def checkInteger(input_case):
    if type(input_case).__name__ != "list":
        return f"custom error: {input_case} is {type(input_case).__name__} not list"
    if len(input_case) == 0:
        return f"custom error: {input_case} is empty" 
    maximum = 10_000_000
    minimum = -10_000_000
    for value in input_case:
        turn_string = str(value)
        if not turn_string.lstrip('-+').isdigit():
            return f"custom error: {value} is not a integer"
        if value >= maximum or minimum >= value:
            return f"custom error: {value} is out of range"
    return True

# https://leetcode.com/problems/merge-sorted-array/description/
# Merge Sorted Array, easy
class MergeSortedArray:
    def merge(self, nums1, m, nums2, n):
        total = list(nums1) + list(nums2) + [m,n]
        checking = checkInteger(total)
        if checking is not True:
            print(checking)
            return
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
        ([1000000000,0], 1, [-1000000000], 1), # too big
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
            find_mas = msa_ds.merge(*eCases)
            if find_mas != None:
                print(find_mas)
        except Exception as error_message:
            print(type(error_message).__name__.replace("Error", " error").lower(), " :",eCases)

get_msa(None)


print()

if input("Next: Remove Duplicates from Sorted Array \ncontinue: ").strip().lower() != "y":
    exit()

print()


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Remove Duplicates from Sorted Array, easy
class RemoveDuplicatesOne:
    def removeDuplicates(self, nums):
        checking = checkInteger(nums)
        if checking is not True:
            print(checking)
            return
        return sorted(list(set(nums)))

rdo_ds = RemoveDuplicatesOne()
def get_rdo(_):
    print("Remove Duplicates from Sorted Array")
    print("happy path")
    print(rdo_ds.removeDuplicates([1,1,2]))
    print(rdo_ds.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(rdo_ds.removeDuplicates([-1,0,0,0,0,3,3]))
    print(rdo_ds.removeDuplicates([2,2,3,4,4,5]))
    print(rdo_ds.removeDuplicates([1,2,3,4,5]))
    print(rdo_ds.removeDuplicates([-1,0,0,0,1,2,2]))
    print(rdo_ds.removeDuplicates([5,6,6,7,8,8,9]))
    print(rdo_ds.removeDuplicates([1,2,2,2,3,3,4,5]))
    print(rdo_ds.removeDuplicates([10,10,10,11,12,13,13,14]))
    print(rdo_ds.removeDuplicates([-3,-2,-2,-1,0,1,1,2,3]))

    print()

    print("corner case")
    print(rdo_ds.removeDuplicates([1]))
    print(rdo_ds.removeDuplicates([1,1,1,1,1]))
    print(rdo_ds.removeDuplicates([-100,-100,-100]))
    print(rdo_ds.removeDuplicates([100,100,100]))
    print(rdo_ds.removeDuplicates([0,0,0,0,0]))
    print(rdo_ds.removeDuplicates([-50]))
    print(rdo_ds.removeDuplicates([100]))
    print(rdo_ds.removeDuplicates([-1,-1,0,0,1,1]))

    print()

    print("monkey test")
    nums = [random.randint(-100,100) for _ in range(100)]
    print(rdo_ds.removeDuplicates(nums))
    nums = [random.choice([0,1,2,3,4,5,6,7,8,9,10]) for _ in range(50)]
    print(rdo_ds.removeDuplicates(nums))
    nums = [random.randint(-5,5) for _ in range(20)]
    print(rdo_ds.removeDuplicates(nums))
    nums = [random.randint(-100,100) for _ in range(1000)]
    print(rdo_ds.removeDuplicates(nums))
    nums = [random.randint(99,100) for _ in range(30)]
    print(rdo_ds.removeDuplicates(nums))

    print()

    print("edge case")
    edges = [
        # TypeError: wrong type
        (), # empty tuple
        (12,1), # tuple not list
        {'a': 1, 'b': 2}, # dict not list
        frozenset({1, 2, 3}), # frozenset not list
        "hello", # string not list
        b"hello", # byte not list
        bytearray(b"hello"), # bytearray not list
        range(3), # range not list
        [1e9,1e9,1e9,1e9,1e9,1e9,1e9,1e9,1e9], # float values, 1e9 is 1000000000.0
        ["hello"], # string to int
        [{"1":"hello"}], # dict in list
        [(1,2,3), 1], # tuple and int in list
        [[1], (2), [{3:3}]], # nested list, int, dict in list
        [1, [2], 2],

        # TypeError: missing argument      
        [], # empty list

        # ValueError: out of range
        [1000000000, 1000000000, 1000000000, 99999999], # too big
        [-1000000000, 99999, -9999999] # too small
    ]


    """
        # Python evaluates test cases before function call, pass arguments as strings to solve the errors
        # ValueError/OverflowError: impossible to calculate
        [i % 9 for i in range(10000000000000000000)]
    """

    for eCases in edges:
        try:
            find_rdo = rdo_ds.removeDuplicates(eCases)
            if find_rdo != None:
                print(find_rdo)
        except Exception as error_message:
            print(type(error_message).__name__.replace("Error", " error").lower(), ":", eCases)

get_rdo(None)