#!/usr/bin/env python3

import sys

current_word = None
current_count = 0
word = None

# Input dari STDIN (output dari mapper.py)
for line in sys.stdin:
    # Hapus spasi di awal dan akhir
    line = line.strip()
    
    # Parse input yang diterima dari mapper.py
    word, count = line.split('\t', 1)
    
    # Konversi count (saat ini sebuah string) ke int
    try:
        count = int(count)
    except ValueError:
        # Jika count bukan angka, abaikan
        continue
    
    # Proses ini bekerja karena input sudah terurut (berdasarkan kata)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Tulis hasil ke STDOUT
            print(f'{current_word}\t{current_count}')
        current_count = count
        current_word = word

# Jangan lupa untuk output kata terakhir jika diperlukan
if current_word == word:
    print(f'{current_word}\t{current_count}')
