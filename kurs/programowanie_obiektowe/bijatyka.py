#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa01.py

class Osoba():
    """ Prosta klasa opisująca osobę """
    
    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp
        
    def ustawPlec(self, imie):
        if imie[-1] == "a":
            self.plec = "k"
            self.atak = 3
            self.blok = 1
        else:
            self.plec = "m"
            self.atak = 5
            self.blok = 3
            
    def atakuj(self, osoba):
        #osoba.hp -= self.atak
        osoba.blokuj(self.atak)
        
    def blokuj(self, atak):
        self.hp -= (atak - self.blok)
        if self.hp < 1:
            print("I'm dead :)")
        else:
            print("i'm still alive!")
        
ala = Osoba('Ala', 'Gwizd', 10)
print(ala.nazwisko, ala.plec, ala.hp)
michal = Osoba('Michaś', 'Świst', 10)
print(michal.nazwisko, michal.plec, michal.hp)

print("Fight: ")

ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)
ala.atakuj(michal)


michal.atakuj(ala)
michal.atakuj(ala)
michal.atakuj(ala)
michal.atakuj(ala)
print(ala.hp, michal.hp)
