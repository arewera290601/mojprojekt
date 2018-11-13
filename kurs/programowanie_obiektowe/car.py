#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
# napisz definicję obiektu samochód z nast. atrybutami:
# marka, np. "Fiat"
# model, np. "Tipo"
#  rok produkcji, np. "2005"
# nadwozie, np. "sedan"
# metody obiektu:
# wiek() - zwraca wiek w latach
from datetime import date

class samochod():
    
    def __init__(self, marka, model, rokp, nadwozie):
        self.marka = marka
        self.model = model
        self.rokp = rokp
        self.nadwozie = nadwozie
        
    def wiek(self):
        return date.today().year - self.rokp

        
samochod = samochod('Fiat', 'Tipo', '2005', 'Sedan')
print("Wiek: ", s.wiek())
