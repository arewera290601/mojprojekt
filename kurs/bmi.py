#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py
#  


def main(args):
        
    masa = float(input('Podaj wagę w kg: '))
    wzrost = int(input('Podaj wzrost w cm: '))
    
    bmi = masa / ((wzrost/100)**2)
    print('BMI = {:.1f}'.format(bmi))
    
    if bmi < 18.5:
        print('Niedowaga')
    elif bmi <= 24.9: 
        print('norma')
    elif bmi < 30:
        print('nadwaga')
    else:
        print('otyłość')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
