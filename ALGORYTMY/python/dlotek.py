#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def main(args):
    ileliczb = int(input("Ile liczb wyrypujesz?"))
    maxliczba = int(input("Podaj maksymalną losowaną liczbę:"))
    print("Wytypuj {} z {} liczb:" .format(ileliczb, maxliczba))

    liczby = []  # definicja pustej listy na losowane liczby
    i = 0  # licznik unikalnych wylosowanych liczb
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maxliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1  # powiększ licznik o 1
    print("Wylosowano:", liczby)

    typy = set()  # def.pustego zbioru na typy użytkownika
    i = 0  # licznik unikalnych typów użytkownika
    while i < ileliczb:
        typ = input("Podaj liczbę {}: ".format(i + 1))
        if typ not in typy:
            typy.add(typ)
            i += 1  # powiększ o 1
    print("Wytypowane:", typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
