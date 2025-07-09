#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

list_append = [1, 2, 3]
list_append.append(4)
print(f"append       : {list_append}")

list_extend = [1, 2, 3]
list_extend.extend([4, 5])
print(f"extend       : {list_extend}")

list_insert = [1, 2, 3]
list_insert.insert(1, 10)
print(f"insert       : {list_insert}")

list_remove = [1, 2, 3, 2]
list_remove.remove(2)
print(f"remove       : {list_remove}")

list_pop = [1, 2, 3]
popped = list_pop.pop()
print(f"pop          : {popped}, list: {list_pop}")

list_pop_i = [1, 2, 3]
popped_i = list_pop_i.pop(1)
print(f"pop(i)       : {popped_i}, list: {list_pop_i}")

list_clear = [1, 2, 3]
list_clear.clear()
print(f"clear        : {list_clear}")
