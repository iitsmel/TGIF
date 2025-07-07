#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

numbers = [1, 2, 3, 4, 5]

mapped = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))
reduced_sum = sum(numbers)

def isOdd(x):
    return x % 2 != 0

filtered_odds = list(filter(isOdd, numbers))
mapped_square = list(map(lambda x: x**2, numbers))

print(f"map (double)          : {mapped}")
print(f"filter (even numbers) : {filtered}")
print(f"sum (reduce)          : {reduced_sum}")
print(f"filter (odd numbers)  : {filtered_odds}")
print(f"map (square)          : {mapped_square}")