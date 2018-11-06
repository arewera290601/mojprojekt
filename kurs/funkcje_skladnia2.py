#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia.py

def mnoz(a, b):
    print(a * b)


def mnoz2(*args):  # zmienna lista argumentów
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)
    

def wylicz(imie1= 'Adam', imie2='Ewa', **kwargs):  # słownik zmiennej długości
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print('{} {}'.format(k, v))    

###################### TYPY ARGUMENTÓW W FUNKCJACH:
# pozycyjne wymagane (wymagane)
# nazwane wymagane (wymagane)
# argumenty domyslne (niewymagane)
# zmiennej długości: listy, słowniki 
####
def main(args):
    # mnoz(4, 3)
    # mnoz2(4, 6, 8, 9, 8, 4, 3, 2, 5)
    wylicz(imie2='Ola', imie3='Alfons', imie4='Piotr')
    return 0
    


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
