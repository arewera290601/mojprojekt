#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto02.py
#  

class Konto():
    def __init__(self, ile=0, dane={}):
        self.bilans = ile
        self.osoba = dane
        
    def wplata(self, ile):
        self.bilans += int(ile)
        return self.bilans
        
    def wyplata(self, ile):
        self.bilans -= int(ile)
        return self.bilans
    
konta = [utworzKonto('Ala'), utworzKonto('Bela')]

    
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
