#!/usr/local/bin/python3
# -*- coding: utf-8 -*

# https://docs.python.org/3/library/functools.html#functools.partial
# https://docs.python.org/3/library/functools.html#functools.singledispatch

from functools import partial, singledispatch

# partial, fix function partially 
def multiply_function(x, y):
    return x * y

partial_function = partial(multiply_function, 3)

# singledispatch, type based dispatch for maintainability
@singledispatch
def singledispatch_function(value):
    return f"non register type (byte) for singledis patch: {value}"

@singledispatch_function.register
def _(value: str):
    return f"{'str':<5}: '{value}', upper: '{value.upper()}'"

@singledispatch_function.register
def _(value: int):
    return f"{'int':<5}: {value}, squared: {value**2}"

@singledispatch_function.register
def _(value: list):
    processed_items = [singledispatch_function(item) for item in value]
    return f"{'list':<5}: [{', '.join(processed_items)}]"

@singledispatch_function.register
def _(value: dict):
    processed_items = [f"{singledispatch_function(k)}: {singledispatch_function(v)}" for k, v in value.items()]
    return f"{'dict':<5}: {{{', '.join(processed_items)}}}"



def main():
    # partial
    print(f"{'partial':<8}: {partial_function(5)}")

    print()

    # singledispatch different type
    print(singledispatch_function(bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])))
    print(singledispatch_function("hi"))
    print(singledispatch_function(2))
    print(singledispatch_function([3, "abc", [4, "def"]]))
    print(singledispatch_function({"a": 5, 6: [7, 8, "ghi"]}))

if __name__ == "__main__":
    main()