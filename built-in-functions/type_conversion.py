#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

integer = 1
floating = 0.1
complex_num = 3 + 4j
string = "A"
boolean = True
bytes_obj = b"byte"
byte_array = bytearray(b"bytearray")
list_obj = [1, 2, 3]
tuple_obj = (4, 5, 6)
set_obj = {7, 8, 9}
frozenset_obj = frozenset({10, 11, 12})
dict_obj = {'key': 'value'}
char = 'A'
ordinal = 65
memory_view = memoryview(b"memory")

print(f"int       : {integer}")
print(f"float     : {floating}")
print(f"complex   : {complex_num}")
print(f"str       : {string}")
print(f"bool      : {boolean}")
print(f"bytes     : {bytes_obj}")
print(f"bytearray : {byte_array}")
print(f"list      : {list_obj}")
print(f"tuple     : {tuple_obj}")
print(f"set       : {sorted(set_obj)}")
print(f"frozenset : {sorted(frozenset_obj)}")
print(f"dict      : {dict_obj}")
print(f"str       : {char}")
print(f"int       : {ordinal}")
print(f"memoryview: {memory_view}")
