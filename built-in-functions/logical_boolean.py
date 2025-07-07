#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

all_true = all([True, True, True])
any_true = any([False, False, True])
all_false = all([False, False, False])
any_false = any([False, False, False])
empty_all = all([])
empty_any = any([])

print(f"all (all True)       : {all_true}")
print(f"any (some True)      : {any_true}")
print(f"all (all False)      : {all_false}")
print(f"any (all False)      : {any_false}")
print(f"all (empty iterable) : {empty_all}")
print(f"any (empty iterable) : {empty_any}")
