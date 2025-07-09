#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

numbers = [1, 2, 3, 4, 5]

sum_numbers = sum(numbers)
lambda_example = lambda a: a + 10
mapped = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print(f"sum                   : {sum_numbers}")
print(f"lamba                 : {lambda_example(1)}")
print(f"map (double)          : {mapped}")
print(f"filter (even numbers) : {filtered}")
