#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos.py

stos = []
SP = 0


def push(rozmiar, dane):
    global stos, SP
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow!")
        SP = rozmiar - 1


def pop(rozmiar):
    global stos, SP
    SP -= 1
    if SP > -1:
        print(stos[SP])
    else:
        print("Out of range!")
        SP = 0


def main(args):
    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu: "))
    stos = [None] * rozmiar
    push(rozmiar, 2)
    push(rozmiar, 3)
    push(rozmiar, 4)
    print("Wskażnik: ", SP)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
