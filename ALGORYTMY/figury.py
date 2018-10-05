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
    
    
    for i in range(a): # pętla zewnętrzna odpowiada za wiersze
       for j in range(b): # pętla wewnętrzna
           if j == 0 or j == b - 1 or i == 0 or i == a - 1:
               print(c, end='')
           else:
               print(" ", end='')
       print() # znak końca linii, tj. przejście do następnego wiersza
    
    return 0

def choinka(h, c):
    h = int(input("Podaj wysokość choinki: "))
    c = str(input("Podaj znak z którego ma byc zbudowana choinka: "))
    
    for i in range(h):
        for j in range(i + 1):
            print(c, end= '')
        print()
    
    return 0
    
def choinka2(h, c):
    h = int(input("Podaj wysokość choinki: "))
    c = str(input("Podaj znak z którego ma byc zbudowana choinka: "))
    
    for i in range(h):
        for j in range(h - i):
            print(c, end= '')
        print()
    
    return 0


def main(args):
    a = int(input("Podaj długość podstawy trójkąta: "))
    h = int(input("Podaj wysokość trojkąta: "))
    c = str(input("Podaj znak z którego ma byc zbudowana trójkąt: "))
    
    for i in range(h):
        for j in range(h + i):
            print(c, end= '')
        print()
  
    
     
            
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
