#!/usr/local/bin/python3

# https://docs.python.org/3/library/base64.html

import base64

raw_data = r""
byte_data = bytes(raw_data, 'utf-8')

try:
    decoded_data = base64.b64decode(byte_data)
    print(decoded_data)
except Exception as e:
    print(f"Error during base64 decoding: {e}")
