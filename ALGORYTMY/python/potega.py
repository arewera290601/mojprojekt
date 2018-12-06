#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  Obliczanie potegi liczby naturalnej 

def potega_re(a, n):
    if n == 0:
        return 1
    returnpotega_re(a, n-1)*a

def potega_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a
        # print(wynik)    
    return wynik
def main(args):
    a = int(input("Podaj liczbę: "))
    n = int(input("Podaj wykładnik: "))
    # a, n = 3, 4 #wielokrotne przypisanie
    # potega_it(a, n) # wywołanie funkcji
    print("Podstawa {} do potęgi {} wynosi {}".
           format(a, n, potega_it(a, n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
