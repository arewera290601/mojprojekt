#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#  



def main(args):
    liczba = int(input('Podaj wartość poczatkową: '))
    liczba2 = int(input('Podaj wartość końcową: '))
    
    while liczba >= liczba2:
        liczba = int(input("Błędny zakres. Podaj poprawny: ")
        
    
        
    for liczba in range(liczba, liczba2 + 1):
        if liczba % 2 == 0 :
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
