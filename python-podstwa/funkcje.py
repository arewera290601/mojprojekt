#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

# zasięg zmiennych  może być lokalny lub globalny
def dodaj(a, b):
    return a + b
def dodaj2(a, b):
    return a - b
def dodaj3(a, b):
    return a * b
def dodaj4(a, b):
    return a / b

def main(args):
    # a = 0 # inicjacja zmiennej
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    # dodaj(a, b) # lub mogę dac 5,6
    
    print("Suma: ", dodaj(a, b))
    print("Różnica: ", dodaj2(a, b))
    print("Iloczyn: ", dodaj3(a, b))
    print("Iloraz: ", dodaj4(a, b))

    return 0

#duck typing
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
