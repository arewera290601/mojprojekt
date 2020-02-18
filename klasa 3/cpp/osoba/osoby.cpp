/* 
 * osoby.cpp
 */

#include <iostream>
#include <cstdlib>
#include "osoba.h"


using namespace std;
int main(int argc, char **argv)
{
        bool sukces = false;
	Osoba o1;
        o1.dane();
        Osoba o2("Adam", "Słodowy", 34, "M");
        o2.dane();
        
        sukces = o2.ustawImie("AARON");
        if (not sukces) {
                cout << "Błąd zmiany imienia" << endl;
        } else {
                o2.dane();
        }
        
        
        sukces = o2.ustawNazwisko("Kowalski");
        if (not sukces) {
                cout << "Błąd zmiany nazwiska" << endl;
        } else {
                o2.dane();
        }
        
        
        sukces = o2.ustawWiek(45);
        if (not sukces) {
                cout << "Błąd zmiany wieku" << endl;
        } else {
                o2.dane();
        }
        
        
        sukces = o2.ustawPlec("K");
        if (not sukces) {
                cout << "Błąd zmiany płci" << endl;
        } else {
                o2.dane();
        }
	return 0;
}

