#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

integer = 1
floating = 0.1
complex_num = 3 + 4j
string = "Hello World!"
character = 'c'
unicode_character = chr(65)
ordinal = ord('A')
boolean = True
bytes_object = b"byte"
byte_array = bytearray(b"bytearray")
list_object = [1, 2, 3]
tuple_object = (4, 5, 6)
set_object = {7, 8, 9}
frozenset_object = frozenset({10, 11, 12})
dictionary_object = {'key': 'value'}
memory_view = memoryview(b"memory")

print(f"int        : {integer}")
print(f"float      : {floating}")
print(f"complex    : {complex_num}")
print(f"str        : {string}")
print(f"char       : {character}")
print(f"char (chr) : {unicode_character}")
print(f"int  (ord) : {ordinal}")
print(f"bool       : {boolean}")
print(f"bytes      : {bytes_object}")
print(f"bytearray  : {byte_array}")
print(f"list       : {list_object}")
print(f"tuple      : {tuple_object}")
print(f"set        : {sorted(set_object)}")
print(f"frozenset  : {sorted(frozenset_object)}")
print(f"dict       : {dictionary_object}")
print(f"memoryview : {memory_view}")
