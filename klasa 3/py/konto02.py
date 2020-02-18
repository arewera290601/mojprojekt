#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto02.py
#  
bilans = 0

while True:
    print('+ - wpłata')
    print('- - wypłata')
    print('0 - koniec')
    op = input('Działanie: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        bilans += int(ile)
    elif op == '-':
        ile = input('Wpłata: ')
        bilans += int(ile)
    else: 
        break
    print("Konto: ", bilans)



print("Konto:", bilans)
