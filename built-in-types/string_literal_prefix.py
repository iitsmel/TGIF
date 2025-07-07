#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

bytes_literal = b'hello'
raw_bytes_literal = br'hello\n'
raw_string_literal = r'hello\n'
unicode_string = 'hello'
formatted_string = f'Hello, {unicode_string}!'
bytearray_literal = bytearray(b'hello')
unicode_escape_string = u'hello'
octal_string = '\141\142\143'
hex_string = '\x61\x62\x63'

print(f"bytes literal         : {bytes_literal}")
print(f"raw bytes literal     : {raw_bytes_literal}")
print(f"raw string literal    : {raw_string_literal}")
print(f"unicode string        : {unicode_string}")
print(f"formatted string (f)  : {formatted_string}")
print(f"bytearray literal     : {bytearray_literal}")
print(f"unicode escape string : {unicode_escape_string}")
print(f"octal escape string   : {octal_string}")
print(f"hex escape string     : {hex_string}")
