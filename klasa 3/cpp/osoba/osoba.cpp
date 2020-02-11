#include <iostream>
#include <cstdlib>
#include "osoba.h"
Osoba::Osoba() {
        imie = nazwisko = plec = "";
        wiek = 0;
}

Osoba::Osoba(string i, string n, int w, string p) {
        imie = i;
        nazwisko = n;
        wiek = w;
        plec = p;
}

void Osoba::dane() {
        cout << imie << " " << nazwisko;
        cout << " (" << wiek << ", ";
        cout << plec << ")" << endl;
}

