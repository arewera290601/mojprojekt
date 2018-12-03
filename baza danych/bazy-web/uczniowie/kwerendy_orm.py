#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
#  
from model_orm import *

def kw01():
    #query = Uczen.select().order_by(Uczen.nazwisko.asc())
    #query = Uczen.select().where(Uczen.imie.startswith('A'))
    #query = Uczen.select().where(Uczen.imie.endswith('a'))
    #query = Uczen.select().where(Uczen.imie == 'Agnieszka')
    query = Uczen.select().where(Uczen.egz_mat.between(30, 35))
    for obj in query:
        print(obj.imie, obj.nazwisko, obj.egz_mat)

def kw02():
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.imie, .order_by(Uczen.klasa.nazwa.asc())
        .join(Klasa)
    )
    for obj in query:
        print(obj.imie, obj.nazwisko, obj.klasa.nazwa)


def main(args):
    baza.connect() # łączenie się z bazą
    
    kw02()
    
    baza.close() # wychodzimy z bazy
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
