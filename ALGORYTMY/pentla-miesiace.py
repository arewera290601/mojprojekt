#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pentla-miesiace.py

def main(args):
	nazwy = ['Styczeń','Luty','Marzec','Kwieceń','Maj','Czerwiec','Lipiec','Sierpień','Wrzesień','Październik','Listopad','Grudzień']

	while 1 > 0:
		numer = int(input("Podaj numer miesiąca: "))
		if numer > 12 or numer < 1:
			print("Wprowadzone dane są błędne! ")
		else:
			print (nazwy[numer - 1])
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
