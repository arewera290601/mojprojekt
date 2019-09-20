#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py


def main(args):
    imie = input('Jak masz na imię?\n')
    nazwisko = input('Jak masz na nazwisko?\n')
    print('Witaj', imie, nazwisko, '!')
   

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
