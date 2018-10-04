#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  program drukuje wypełniony prostokąt o bokach podanych przez uytkowniaka za pomoca podanego znaku


def prostokat1(a, b, c): #drukowanie wypełnionego prostokąta
    a = int(input("Podaj szerokość prostokąta: "))
    b = int(input("Podaj wysokość prostokata: "))
    c = str(input("Podaj znak prostokata: "))
    
    i=0
    j=0
    
    for i in range(a): #petla zewnetrzna
        for j in range(b): #petla wewnetrzna
            print(c, end='')
        print() # znak konca linii, tj. przejscie do nast. wiersza
        
    return 0
    
def prostokat2(a, b, c): #drukowanie pustego prostokąta
    a = int(input("Podaj szerokość prostokąta: "))
    b = int(input("Podaj wysokość prostokata: "))
    c = str(input("Podaj znak prostokata: "))
    
    
    for i in range(a):
        for j in range(b):
            if i 
            if j == 0 or j == b - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()
    
    return 0
    
def main(args):
    a = int(input("Podaj szerokość prostokąta: "))
    b = int(input("Podaj wysokość prostokata: "))
    c = str(input("Podaj znak prostokata: "))
    
    
    for i in range(a):
        for j in range(b):
            if i 
            if j == 0 or j == b - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
