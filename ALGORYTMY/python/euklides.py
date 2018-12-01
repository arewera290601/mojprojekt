#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#  
def nwd1(a, b):
    while a != b: # ten operator mówi że dopóki a jest różne od b
       if a > b:
          a = a - b
       else:
          b = b - a
    # print(a)
    return a
    
def main(args):
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    
    print("Najwyższy wspólny dzielnik dla {} i {} = {}". format (
                                                                a,
                                                                b,
                                                                nwd1(a, b)
                                                                ))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
