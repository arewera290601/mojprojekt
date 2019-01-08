#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py

import os
from peewee import *

baza_plik = 'test_orm.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Wynik(BazaModel):
    egz_hum = DecimalField(default=0)
    egz_mat = DecimalField(default=0)
    egz_jez = DecimalField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl1 = Klasa(nazwa='2A', roknaboru=2012, rokmatury=2015)
    kl1.save()
    kl2 = Klasa(nazwa='1A', roknaboru=2013, rokmatury=2016)
    kl2.save()
    kl3 = Klasa(nazwa='3A', roknaboru=2011, rokmatury=2014)
    kl3.save()
    
    #kl2a= Klasa.select().where(Klasa.nazwa=='2A').get()
    u1= Uczen(imie='Jan', nazwisko='Kowalski', plec=False, klasa=kl1)#kl2a
    u1.save()
    u2= Uczen(imie='Paulina', nazwisko='Noga', plec=True, klasa=kl2)
    u2.save()
    u3= Uczen(imie='Mateusz', nazwisko='Rewera', plec=False, klasa=kl3)
    u3.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.imie, uczen.nazwisko)
    
    klasa = Klasa.select()
    for klasa in Klasa:
        print(klasa.id, klasa.nazwa, klasa.roknaboru, klasa.rokmatury)
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
