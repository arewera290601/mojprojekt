#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py

import turtle as t

def figura(bok, kat, ile):
    for i in range(ile):
        t.forward(bok)
        t.right(kat)
        
        
def figura_rek(bok, kat, ile, krok):
    t.forward(bok)
    t.right(kat)
    print(ile)
    if ile > 0:  # warunek brzegowy
        figura_rek(bok - krok, kat, ile - 1, krok)
    
def main(args):
    t.setup(800, 600)
    t.color('gold', 'green')
    t.begin_fill()
    t.speed(0)
    
    figura_rek(100, 70, 80, 5)
    
    t.end_fill()
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
