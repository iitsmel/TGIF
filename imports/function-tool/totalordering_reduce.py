#!/usr/local/bin/python3
# -*- coding: utf-8 -*

# https://docs.python.org/3/library/functools.html#functools.total_ordering
# https://docs.python.org/3/library/functools.html#functools.reduce

from functools import total_ordering, reduce

# total ordering, generate the following based on __eq__ and either __lt__ or __le__ or __gt__ or __ge__
@total_ordering
class TestCase:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    # equal
    def __eq__(self, other):
        if not isinstance(other, TestCase):
            return NotImplemented
        return self.priority == other.priority
    
    # less than
    def __lt__(self, other):
        if not isinstance(other, TestCase):
            return NotImplemented
        return self.priority < other.priority

    # greater than
    def __gt__(self, other):
        if not isinstance(other, TestCase):
            return NotImplemented
        return self > other

    # greater than or equal to
    def __ge__(self, other):
        if not isinstance(other, TestCase):
            return NotImplemented
        return not self < other

    # less than or equal to
    def __le__(self, other):
        if not isinstance(other, TestCase):
            return NotImplemented
        return not other < self
    
    # string representation
    def __repr__(self):
        return f"{self.name}(priority={self.priority})"


# reduce, combine all items in a sequence into a single value
reduce_adding = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) # ((((1+2)+3)+4)+5)
reduce_multiplying = reduce(lambda x, y: x*y, [1, 2, 3, 4, 5]) # ((((1*2)*3)*4)*5)
reduce_custom = reduce(lambda x, y: x*(x+y), [1, 2, 3, 4, 5]) # ((((1*(1+2))*((1*(1+2))+3))*(((1*(1+2))*((1*(1+2))+3))+4))*((((1*(1+2))*((1*(1+2))+3))*(((1*(1+2))*((1*(1+2))+3))+4))+5))


def main():
    # total_ordering
    tests = [
        TestCase("first number", 2),
        TestCase("second number", 1),
        TestCase("third number", 3),
    ]
    print(f"{'total ordering tests by priority:'} {sorted(tests)}")

    print()

    # reduce
    print(f"{'reduce adding':<25}: {reduce_adding}")
    print(f"{'reduce multiplying':<25}: {reduce_multiplying}")
    print(f"{'reduce custom combination':<25}: {reduce_custom}")

if __name__ == "__main__":
    main()