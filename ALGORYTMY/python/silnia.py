#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  Obliczanie silni liczby naturalnej 

def silnia_it(n):
    """
    n! = 1 * 2 * ... * n
    """
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
        # print(wynik)    
    return wynik
def main(args):
    n = int(input("Podaj liczbę: "))
    # a, n = 3, 4 #wielokrotne przypisanie
    # potega_it(a, n) # wywołanie funkcji
    print("{}! silnia wynosi {}".
           format(n, silnia_it(n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
