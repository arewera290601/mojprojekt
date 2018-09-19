#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

def trojkat(a, b, c):
    """Funkcja bada możliwość zbudowania trójkąt z trzech podanych boków 
   Funkcja zwraca True jeżeli się da, false w przeciwnym wypadku """ 
  
  
    if a + b > c and b + c > a and a + c > b:
        return True
  
    return False

def main(args):
    #a = int(input('Podaj 1. bok: '))
    #print(a)
    #b = int(input('Podaj 2. bok: '))
    #print(b)
    #c = int(input('Podaj 3. bok: '))
    #print(c)
    
    #if trojkat(a, b, c):
     #   print("Da się")
    #else:
     #   print("Nie da się")
    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
