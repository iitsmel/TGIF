#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/bisect.html

import bisect

bisect_list = [1, 3, 4, 7, 9]
print(f"{"original list":<45}: {bisect_list}")

pos = bisect.bisect(bisect_list, 5)
print(f"{"bisect find insertion position (5) ":<45}: {bisect_list}")

bisect.insort(bisect_list, 5)
print(f"{"insort inset & maintain order (5) ":<45}: {bisect_list}")

bisect.insort_left(bisect_list, 7)
print(f"{"insort_left (7) ":<45}: {bisect_list}")

bisect.insort_right(bisect_list, 7)
print(f"{"insort_right (7) ":<45}: {bisect_list}")

print(f"{"bisect_left leftmost insertion point (5) ":<45}: {bisect.bisect_left(bisect_list, 5)}")

print(f"{"position_right rightmost insertion point (5) ":<45}: {bisect.bisect_right(bisect_list, 5)}")

