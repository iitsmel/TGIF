#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

sample_list = [1, 2, 3]
sample_string = "abc"
sample_integer = 42
sample_dictionary = {"x": 1}
sample_set = {1, 2, 3}

type_list = type(sample_list).__name__
type_string = type(sample_string).__name__
type_int = type(sample_integer).__name__
identifier_string = id(sample_string)
dictionary_string = dir(sample_string)  # list of attributes/methods
string_int = str(sample_integer)
representation_int = repr(sample_integer)
check_string_yes = hasattr(sample_string, "__contains__") # string representation of an object
check_string_no = hasattr(sample_integer, "__contains__")

print(f"type (list)          : {type_list}")
print(f"type (str)           : {type_string}")
print(f"type (int)           : {type_int}")
print(f"id   (str)           : {identifier_string}")
print(f"dir  (str, first 7)  : {dictionary_string[:7]} and more")
print(f"str  (int)           : {string_int}")
print(f"repr (int)           : {representation_int}")
print(f"hasattr ({sample_string}, '__contains__'): {check_string_yes}")
print(f"hasattr ({sample_integer}, '__contains__') : {check_string_no}")
