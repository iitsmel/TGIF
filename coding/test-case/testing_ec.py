#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

unicode_case = r'("\U000FFFFE", "city10\U000FFFEprivate")'
string_case = r'("float", "f" * int(1e308))'

print(f"{'unicode case':<15}: {unicode_case}")
print(f"{'string case':<15}: {string_case}")

