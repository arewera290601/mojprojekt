#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto02.py
#  
bilans = 0

def utworzKonto(imie):
    return {'kto': imie.lower(), 'bilans': 0}

def wplata(klient):
    ile = input('Wpłata: ')
    klient['bilans'] += int(ile)
    return klient
    
def wyplata(klient):
    ile = input('Wypłata: ')
    klient['bilans'] -= int(ile)
    return klient
    
konta = [utworzKonto('Ala'), utworzKonto('Bela')]
kto = None
    
while True:
    if not kto:
        kto=input('Imię: ').strip().lower()
        klient = None
        for o in konta:
            if o['kto'] == kto:
                klient = o
        if not klient:
            print('Nie ma konta!')
            kto = None
            continue
    print('+ - wpłata')
    print('- - wypłata')
    print('0 - koniec')
    op = input('Działanie: ').strip()
    if op == '+':
        klient = wplata(klient)

    elif op == '-':
        klient = wyplata(klient)
    else: 
        break
    print("Konto: ", klient['kto'], ':', konto['bilans'])



print("Konto:", bilans)
