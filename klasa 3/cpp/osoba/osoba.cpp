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

bool Osoba::ustawImie(string i) {
        if (i.size() > 1) {
                imie = i;
                return true;
        }
        return false;
}

bool Osoba::ustawNazwisko(string n) {
        if (n.size() > 1) {
                nazwisko = n;
                return true;
        }
        return false;
}

bool Osoba::ustawWiek(int w) {
        if (w > 0) {
                wiek = w;
                return true;
        }
        return false;
}

bool Osoba::ustawPlec(string p) {
        if (p.size() > 0) {
                plec = p;
                return true;
        }
        return false;
}
