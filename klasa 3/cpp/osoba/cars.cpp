#include <iostream>
#include <cstdlib>
#include "osoba.h"
#include "car.h"

using namespace std;

int main(int argc, char **argv)
{
        bool sukces = false;
	Car c1;
        c1.dane();
        Car c2("AUDI", "A6/B5", 2015, 20000, 5);
        c2.dane();
        
        sukces = c2.ustawMarke("OPEL");
        if (not sukces) {
                cout << "Błąd zmiany marki" << endl;
        } else {
                c2.dane();
        }
        
        
        sukces = c2.ustawModel("Astra");
        if (not sukces) {
                cout << "Błąd zmiany modelu" << endl;
        } else {
                c2.dane();
        }
        
        
        sukces = c2.ustawRocznik(2010);
        if (not sukces) {
                cout << "Błąd zmiany rocznika" << endl;
        } else {
                c2.dane();
        }
        
        
        sukces = c2.ustawPrzebieg(200000);
        if (not sukces) {
                cout << "Błąd zmiany przebiegu" << endl;
        } else {
                c2.dane();
        }

        sukces = c2.ustawIleosob(9);
        if (not sukces) {
                cout << "Błąd zmiany liczby osób" << endl;
        } else {
                c2.dane();
        }
	return 0;
}


