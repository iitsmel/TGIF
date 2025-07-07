#!/usr/local/bin/python3

# https://docs.python.org/3/howto/unicode.html

import unicodedata
import urllib.parse

# howto
char = 'A'
print(f"Character: '{char}'")
print(f"Name     : {unicodedata.name(char)}")
print(f"Category : {unicodedata.category(char)}")

if input("Proceed to payload automation? (y/n): ").strip().lower() != 'y':
    exit()

# payload automation
original_payload = '../payloads/unicode.txt'
fuzz_payload = '../payloads/unicode_fuzz.txt'

encodings = [
    'latin1', 'utf-8', 'utf-16', 'utf-16le', 'utf-16be',
    'utf-32', 'utf-32le', 'utf-32be',
    'ascii', 'cp1252', 'iso8859_1', 'iso8859_15', 'mac_roman',
    'utf_7', 'utf_8_sig', 'big5', 'gbk', 'shift_jis',
    'euc_jp', 'euc_kr', 'koi8_r', 'koi8_u'
]

with open(original_payload, 'r') as current_file, open(fuzz_payload, 'wb') as output_file:
    for line in current_file:
        payload = line.strip()
        if not payload:
            continue
        bytes_sequence = urllib.parse.unquote_to_bytes(payload)
        for encoding in encodings:
            try:
                decoded = bytes_sequence.decode(encoding)
                output_file.write(decoded.encode(encoding) + b'\n')
            except Exception:
                pass