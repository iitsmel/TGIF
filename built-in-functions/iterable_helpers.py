#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

length = len([1, 2, 3])
enumerated = list(enumerate(['a', 'b', 'c']))
zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))
sorted_list = sorted([3, 1, 2])
reversed_list = list(reversed([1, 2, 3]))
all_true = all([True, True, False])
any_true = any([False, False, True])
filtered = list(filter(lambda x: x > 1, [0, 1, 2, 3]))
mapped = list(map(lambda x: x * 2, [1, 2, 3]))
next_item = next(iter([10, 20, 30]))
iterator = iter([4, 5, 6])
sliced = [1, 2, 3, 4, 5][slice(1, 4)]
summed = sum([1, 2, 3, 4])

print(f"len       : {length}")
print(f"enumerate : {enumerated}")
print(f"zip       : {zipped}")
print(f"sorted    : {sorted_list}")
print(f"reversed  : {reversed_list}")
print(f"all       : {all_true}")
print(f"any       : {any_true}")
print(f"filter    : {filtered}")
print(f"map       : {mapped}")
print(f"next      : {next_item}")
print(f"iter      : {list(iterator)}")  # consume iterator for printing
print(f"slice     : {sliced}")
print(f"sum       : {summed}")