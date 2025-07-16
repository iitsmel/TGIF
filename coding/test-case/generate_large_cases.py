#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

large_list = [1] * 2025
filename = input("enter filename (with extension): ")

with open(filename, 'w') as f:
    f.write(str(large_list))
