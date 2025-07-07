#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/itertools.html

from itertools import (
    count, cycle, repeat, accumulate, batched,
    chain, compress, dropwhile, filterfalse,
    groupby, islice, pairwise, starmap,
    takewhile, tee, zip_longest,
    product, permutations, combinations, combinations_with_replacement
)

count_values = []
for i in count(10):
    if i > 14:
        break
    count_values.append(i)
print(f"{'count':20}: {count_values}")

cycled_values = []
cycler = cycle('ABCD')
for _ in range(8):
    cycled_values.append(next(cycler))
print(f"{'cycle':20}: {cycled_values}")

repeated_values = list(repeat(10, 3))
print(f"{'repeat':20}: {repeated_values}")

accumulated_values = list(accumulate([1, 2, 3, 4, 5]))
print(f"{'accumulate':20}: {accumulated_values}")

batched_values = list(batched('ABCDEFG', 3))
print(f"{'batched':20}: {batched_values}")

chained_values = list(chain('ABC', 'DEF'))
print(f"{'chain':20}: {chained_values}")

chain_from_iterable_values = list(chain.from_iterable(['ABC', 'DEF']))
print(f"{'chain.from_iterable':20}: {chain_from_iterable_values}")

compressed_values = list(compress('ABCDEF', [1, 0, 1, 0, 1, 1]))
print(f"{'compress':20}: {compressed_values}")

dropped_values = list(dropwhile(lambda x: x < 5, [1, 4, 6, 3, 8]))
print(f"{'dropwhile':20}: {dropped_values}")

filterfalse_values = list(filterfalse(lambda x: x < 5, [1, 4, 6, 3, 8]))
print(f"{'filterfalse':20}: {filterfalse_values}")

groupby_results = []
for key, group in groupby(['A', 'B', 'DEF'], len):
    groupby_results.append((key, list(group)))
print(f"{'groupby':20}: {groupby_results}")

islice_values = list(islice('ABCDEFG', 2, None))
print(f"{'islice':20}: {islice_values}")

pairwise_values = list(pairwise('ABCDEFG'))
print(f"{'pairwise':20}: {pairwise_values}")

starmap_values = list(starmap(pow, [(2, 5), (3, 2), (10, 3)]))
print(f"{'starmap':20}: {starmap_values}")

takewhile_values = list(takewhile(lambda x: x < 5, [1, 4, 6, 3, 8]))
print(f"{'takewhile':20}: {takewhile_values}")

tee_iter1, tee_iter2 = tee([1, 2, 3])
print(f"{'tee it1':20}: {list(tee_iter1)}")
print(f"{'tee it2':20}: {list(tee_iter2)}")

zip_longest_values = list(zip_longest('ABCD', 'xy', fillvalue='-'))
print(f"{'zip_longest':20}: {zip_longest_values}")

product_values = list(product([1, 2], ['a', 'b']))
print(f"{'product':20}: {product_values}")

permutations_values = list(permutations([1, 2, 3], 2))
print(f"{'permutations':20}: {permutations_values}")

combinations_values = list(combinations([1, 2, 3], 2))
print(f"{'combinations':20}: {combinations_values}")

combinations_with_replacement_values = list(combinations_with_replacement([1, 2, 3], 2))
print(f"{'combinations_with_replacement':20}: {combinations_with_replacement_values}")
