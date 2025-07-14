#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/collections.html

from collections import (
    namedtuple, deque, ChainMap, Counter, OrderedDict, 
    defaultdict, UserDict, UserList, UserString
)

# deque: list like container with fast appends and pops on either end
print("deque")
dq = deque([1,2,3])
dq.append(4)
print(f"{'append':<20}: {list(dq)}")
dq.appendleft(0)
print(f"{'append left':<20}: {list(dq)}")
dq_copy = dq.copy()
dq.clear()
print(f"{'clear':<20}: {list(dq)}")
dq_count = dq_copy.count(0) # count the number of deque elements equal to x
print(f"{'count':<20}: {dq_count}")
dq_copy.extend([9])
print(f"{'extend':<20}: {list(dq_copy)}")
dq_copy.extendleft([-1])
print(f"{'extend left':<20}: {list(dq_copy)}")
print(f"{'1 index':<20}: {dq_copy.index(1)}") # return the position of x in the deque
dq_copy.insert(-1, 5)
print(f"{'insert':<20}: {list(dq_copy)}")
popped = dq_copy.pop()
print(f"{'pop':<20}: {popped}, {list(dq_copy)}")
popped_left = dq_copy.pop()
print(f"{'pop left':<20}: {popped_left}, {list(dq_copy)}")
dq_copy.remove(1)
print(f"{'remove 1':<20}: {list(dq_copy)}")
dq_copy.reverse()
print(f"{'reverse':<20}: {list(dq_copy)}")
dq_copy.rotate(1)
print(f"{'rotate right 1':<20}: {list(dq_copy)}")
dq_copy.rotate(-1)
print(f"{'rotate left -1':<20}: {list(dq_copy)}")
dq_maxLen = deque([1,2,3], maxlen=3)
print(f"{'maxlen 3':<20}: {dq_maxLen.maxlen}")
print(f"{'maxlen unbound':<20}: {dq_copy.maxlen}")

print()

# namedtuple: factory function for creating tuple subclasses with named fields
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'California')
print(f"{'namedtuple':<20}: {person}")

print()

# Counter: dict subclass for counting hashable objects
counter = Counter('abracadabra')
print(f"{'Counter abracadabra':<20}: {dict(counter)}")

print()

# defaultdict: dict subclass that calls a factory function to supply missing values
dd = defaultdict(list)
dd['alphabets'].append('a')
dd['alphabets'].append('b')
dd['numeric'].append('1')
print(f"{'defaultdict':<20}: {dict(dd)}")

print("\n\n")

print("overkill modules, don't need them most of the time")

print()

# OrderedDict: dict subclass that remembers the order entries were added
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print("Just use dict")
print(f"{'OrderedDict item':<20}: {list(od.items())}")

print()

print("wrapping and unwrapping data without any custom behavior")
# UserDict: wrapper around dictionary objects for easier dict subclassing
dict_for_userdict = {'a':1,'b': 2,'c': 3}
ud = UserDict(dict_for_userdict)
print(f"{'UserDict data':<20}: {dict(ud.data)}")

# UserList: wrapper around list objects for easier list subclassing
list_for_userlist = [1,2,3]
ul = UserList(list_for_userlist)
print(f"{'UserList data':<20}: {list(ul.data)}")

# UserString: wrapper around string objects for easier string subclassing
us = UserString("hello world")
print(f"{'UserString':<20}: {str(us)}")

print()

# ChainMap: dict like class for creating a single view of multiple mappings
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
cm = ChainMap(dict1, dict2)
print("{**dict1, **dict2} is cleaner")
print(f"{'ChainMap (dict)':<20}: {dict(cm)}")