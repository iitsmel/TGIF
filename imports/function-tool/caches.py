#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/functools.html
# https://docs.python.org/3/library/profile.html
# https://docs.python.org/3/library/tracemalloc.htmls

import cProfile
import tracemalloc
import functools

# least recently used cache
# lru_cache(maxsize=None) equals to cache(), LRU feature is disabled and the cache can grow without bound
# https://stackoverflow.com/questions/61536704/why-does-python-lru-cache-performs-best-when-maxsize-is-a-power-of-two
@functools.lru_cache(maxsize=2**20, typed=True)
def lru_cache_function_seperate(number_input):
    return computation(number_input)

@functools.lru_cache(maxsize=2**20, typed=False)
def lru_cache_function_not_seperate(number_input):
    return computation(number_input)

# cache
# memory time trade off, fast but consumes memory
@functools.cache
def cache_this_function(number_input):
    return computation(number_input)

# cached_property
# first time expensive
class CachedPropertyDataSet:
    def __init__(self, number_input):
        self.num_input = number_input

    @functools.cached_property
    def cached_property_method(self):
        return computation(self.num_input)

cp_ds = CachedPropertyDataSet(100000)
def get_cached_property_method(_):
    return cp_ds.cached_property_method



def profiling_function(target_function, function_input_value, profile_lable, hit_or_miss):
    # calculation for time and space complexity
    tracemalloc.start()
    profiler = cProfile.Profile()
    profiler.enable()

    target_function(function_input_value)

    profiler.disable()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # sum cumulative (total) time from code objects (co_name) matching target function’s name
    profiler_status = profiler.getstats()
    cumtime = 0.0
    for current_status in profiler_status:
        if hasattr(current_status.code, "co_name") and current_status.code.co_name == target_function.__name__:
            cumtime += current_status.totaltime
    
    print(
        f"{profile_lable:<33} {hit_or_miss:<6}"
        f"cumtime: {cumtime:>8f} s  memory: {current_memory / 1024:8f} KB | Peak: {peak_memory / 1024:8f} KB"
    )

def computation(number_input):
    total = 0
    for i in range(1, number_input):
        total += (i * i) % 1234567
    return total

def main():
    number_input = 1000000

    # lru_cache(typed=True)
    lru_cache_function_seperate.cache_clear()
    profiling_function(lru_cache_function_seperate, number_input, "lru_cache_function_separate", "miss")
    profiling_function(lru_cache_function_seperate, number_input, "lru_cache_function_separate", "hit")
    print()

    # lru_cache(typed=False)
    lru_cache_function_not_seperate.cache_clear()
    profiling_function(lru_cache_function_not_seperate, number_input, "lru_cache_function_not_separate", "miss")
    profiling_function(lru_cache_function_not_seperate, number_input, "lru_cache_function_not_separate", "hit")
    print()

    # cache
    cache_this_function.cache_clear()
    profiling_function(cache_this_function, number_input, "cache_this_function", "miss")
    profiling_function(cache_this_function, number_input, "cache_this_function", "hit")
    print()

    # cached_property
    profiling_function(get_cached_property_method, None, "DataSet.cached_property", "miss")
    profiling_function(get_cached_property_method, None, "DataSet.cached_property", "hit")

if __name__ == "__main__":
    main()