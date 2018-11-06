#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia.py
#  

a, b = 5, 10 # zmienna(variable) globalna , zasięg(global) globalny, przestrzeń(namespace) nazw modułu
print('7:', a+b)


def sumuj1(): # nowa przestrzeń nazw, przestrzeń funkcji
    print('12:', a + b)


def main(args):
    global a,b
    a, b = 2, 3 # zmienne lokalne, zasięg lokalny, przestrzeń funkcji
    print('17:', a + b)
    sumuj1() # wywołanie funkcji
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
