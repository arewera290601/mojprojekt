#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py



def main(args):
    # a = 0 # inicjacja zmiennej
   a = int(input('Podaj 1. liczbę: '))
   print(a)
   b = int(input('Podaj 2. liczbę: '))
   print(b)
   
   if a > b: 
       print(a,"jest większe od", b)
   elif b > a: 
       print(b,"jest większe od", a)
   else:  
       print(a,"równa się", b)
   return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
