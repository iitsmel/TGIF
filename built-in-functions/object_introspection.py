#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

sample_list = [1, 2, 3]
sample_str = "abc"
sample_int = 42
sample_dict = {"x": 1}
sample_set = {1, 2, 3}

type_list = type(sample_list).__name__
type_str = type(sample_str).__name__
type_int = type(sample_int).__name__
id_str = id(sample_str)
dir_str = dir(sample_str)  # list of attributes/methods
repr_int = repr(sample_int)
str_int = str(sample_int)

print(f"type (list)           : {type_list}")
print(f"type (str)            : {type_str}")
print(f"type (int)            : {type_int}")
print(f"id (str)              : {id_str}")
print(f"dir (str, first 7)    : {dir_str[:7]} ...")
print(f"repr (int)            : {repr_int}")
print(f"str (int)             : {str_int}")
