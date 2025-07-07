#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

lst_append = [1, 2, 3]
lst_append.append(4)
print(f"append       : {lst_append}")

lst_extend = [1, 2, 3]
lst_extend.extend([4, 5])
print(f"extend       : {lst_extend}")

lst_insert = [1, 2, 3]
lst_insert.insert(1, 10)
print(f"insert       : {lst_insert}")

lst_remove = [1, 2, 3, 2]
lst_remove.remove(2)
print(f"remove       : {lst_remove}")

lst_pop = [1, 2, 3]
popped = lst_pop.pop()
print(f"pop          : {popped}, list: {lst_pop}")

lst_pop_i = [1, 2, 3]
popped_i = lst_pop_i.pop(1)
print(f"pop(i)       : {popped_i}, list: {lst_pop_i}")

lst_clear = [1, 2, 3]
lst_clear.clear()
print(f"clear        : {lst_clear}")
