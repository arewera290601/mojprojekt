#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  warunki.py
# program pobiera 3 liczby7 całkowite
# i wyświetla loiczbę największą

def maks(a, b, c):
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c
    
    return maks

def main(args):
    # a = 0 # inicjacja zmiennej
   a = int(input('Podaj 1. liczbę: '))
   print(a)
   b = int(input('Podaj 2. liczbę: '))
   print(b)
   c = int(input('Podaj 3. liczbę: '))
   print(c)
   
   assert(maks(3, 2, 1) == 3)
   assert(maks(2, 3, 1) == 3)
   assert(maks(1, 2, 3) == 3)
   assert(maks(1, 1, 3) == 3)
   assert(maks(3, 3, 1) == 3)
   assert(maks(3, 3, 3) == 3)
   assert(maks(3, 1, 1) == 3)
   
   if b <= a >= c:
       print(a,"jest największe")
   elif a <= b >=c: 
       print(b,"jest największe")
   else:  
       print(c,"jest największe")
   return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
