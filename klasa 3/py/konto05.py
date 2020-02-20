#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  konto02.py
#  

class KontoBasic():
    def __init__(self, ile=0, dane={}):
        self.bilans = ile
        self.osoba = dane
        
    def wplata(self, ile):
        self.bilans += int(ile)
        return self.bilans
        
    def wyplata(self, ile):
        self.bilans -= int(ile)
        return self.bilans
        
    def getDane(self, k):
        return self.osoba[k]
    
    def drukujBilans(self):
        print(self.bilans)
        
k1 = KontoBasic(100, {'imie': 'Adam', 'nazwisko': 'Słodowy'})
k2 = KontoBasic(2000, {'imie': 'Izabela', 'nazwisko': 'Kowalsky'})

k1.wplata(100)
k2.wplata(3000)
k1.wyplata(200)
k2.wyplata(400)
print(k2.getDane('imie')) 
k2.drukujBilans()


class KontoPremium(KontoBasic):
    def __init__(self, ile, dane={}, debet=0):
        KontoBasic.__init__(self, ile, dane) #wywołanie konstruktora rodzica
        self.debet = debet
    
    def wyplata(self, ile):
        if self.bilans - ile < self.debet:
            print('Brak środków!')
            return self.bilans
        else: 
            return KontoBasic.wyplata(self, ile)
            
k1 = KontoPremium(0, {'imie': 'Adam', 'nazwisko': 'Słodowy'}, -50)
k2 = KontoPremium(0, {'imie': 'Izabela', 'nazwisko': 'Kowalsky'}, -100)

k1.wplata(100)
print(k1.wyplata(200))

k2.wplata(10)
print(k2.wyplata(20))
