#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

# zasięg zmiennych  może być lokalny lub globalny
def suma(a, b):
    return a + b
    
def roznica(a, b):
    return a - b
    
def iloczyn(a, b):
    return a * b
    
def iloraz(a, b):
    return a / b

def main(args):
    # a = 0 # inicjacja zmiennej
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    # dodaj(a, b) # lub mogę dac 5,6
    
    print("Suma: ", suma(a, b))
    print("Różnica: ", roznica(a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))

    return 0

#duck typing
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
