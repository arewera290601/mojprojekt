#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py
#  



def main(args):
    Vk = input('Podaj rozmiar danych skompresowanych (Bajty): ')
    Vnk = input('Podaj rozmiar danych nieskompresowanych (Bajty): ')
    Rc = int(Vk) / int(Vnk) * 100
    Rc2 = (1 -  int(Vk) / int(Vnk)) * 100
    print ('Wspólczynnik kompresji: ', Rc)
    print ('O ile zmniejszyły się dane: ', Rc2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
