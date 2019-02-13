#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kodmorsa.py
#  
 
kod = {'a': '+-', 'ą':'+-+-', 'b':'-+++', 'c':'-+-+', 'ć':'-+-++', 'd':'-++', 'e':'+', 'ę':'++-++', 
       'f':'++-+', 'g':'--+', 'h':'++++', 'i':'++', 'j':'+---', 'k':'-+-', 'l':'+-++', 'ł':'+-++-', 
       'm':'--', 'n':'-+', 'ń':'--+--', 'o':'---', 'ó':'--+', 'p':'+--+', 'q':'--+-', 'r':'+-+', 's':'+++',
       't':'-', 'u':'++-', 'v':'+++-', 'w':'+--',
       'x':'-++-', 'y':'-+--', 'z':'--++', 'ch':'----', 'ś':'+++-+++', 'ż':'--++-+', 'ź':'--++-'}

def koduj(tekst):
    for l in tekst:
        print(kod[l])
        
def dekoduj():
    tekst = []
    lit = ' '
    while lit > '':
        lit = input('Podaj kod Morsea: ')
        tekst.append(lit)
    print(tekst)

def odwrotnie():
    tekst = []
    lit = ' '
    

def main(args):
    # ~tekst = input('Podaj tekst: ').lower()
    # ~print("".join([kod[l] for l in tekst])) 
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
