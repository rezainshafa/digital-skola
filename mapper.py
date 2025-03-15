#!/usr/bin/env python3

import sys
import re

# Input dari STDIN (standard input)
for line in sys.stdin:
    # Hapus spasi di awal dan akhir
    line = line.strip()
    
    # Pisahkan baris menjadi kata-kata (tanpa mengubah menjadi lowercase)
    # dan biarkan karakter non-alfanumerik
    words = re.split(r'\s+', line)
    
    # Output adalah pasangan kata dan angka 1 untuk setiap kata
    for word in words:
        if word:  # Hanya proses kata non-kosong
            print(f'{word}\t1')
