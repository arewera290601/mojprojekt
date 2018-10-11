#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py
#  

def liczby2():
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe 
    w których cyfry nie powtarzają się. 
    Funkcja zwraca ich liczbę. 
    Wykluczone liczby: 11, 22, 33, 44, 55, 66, 77, 88, 99.
    """
    ile = 0 #licznik
    for i in range(1, 10):
        for j in range(0, 10):
            if i == j:
                print("-", '', end= '')
            else:
                print("{}{} ".format(i, j), end= '')
                ile = ile +1
    print()
    return ile
def liczby3():
    """
    Funkcja drukuje wszystkie liczby trzycyfrowe 
    w których cyfry nie powtarzają się. 
    Funkcja zwraca ich liczbę. 
    Wykluczone liczby: 111, 222, 333, 444, 555, 666, 777, 888, 999, 110, 122, 100.
    """
    ile = 0
    for i in range(1, 10): # cyfra setek
        for j in range(0, 10): # cyfra dziesiątek
            for k in range(0, 10): # cyfra jedności
                if i == j or i == k or j == k: # if i != k and i != j and j!=k i wtedy bez else 
                    print("-", '', end= '')
                else:
                    print("{}{}{} ".format(i, j, k), end= '')
                    ile = ile +1
    print()
    return ile
def main(args):
    print("Liczb 2-cyfrowych: ", liczby2())
    print("Liczb 3-cyfrowych: ", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
