#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto02.py
#  
bilans = 0


def wplata(ile, bilans):
    ile = input('Wpłata: ')
    bilans += int(ile)
    return bilans
    
def wyplata(ile, bilans):
    ile = input('Wypłata: ')
    bilans -= int(ile)
    return bilans
    
    
while True:
    print('+ - wpłata')
    print('- - wypłata')
    print('0 - koniec')
    op = input('Działanie: ').strip()
    if op == '+':
        bilans = wplata(bilans)

    elif op == '-':
        bilans = wyplata(bilans)
    else: 
        break
    print("Konto: ", bilans)



print("Konto:", bilans)
