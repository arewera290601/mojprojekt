#include <iostream>
#include <cstdlib>
#include "osoba.h"

#ifndef __CAR_H_
#define __CAR_H_

using namespace std;

class Car{
private:
    string marka;
    string model;
    int rocznik;
    int przebieg;
    int ileosob; 
    Osoba osoby[3];
public:
    Car();
    Car(string, string, int, int, int);
    void dane();
    bool ustawMarke(string);
    bool ustawModel(string);
    bool ustawRocznik(int);
    bool ustawIleosob(int);
    void dodaj();
    void pasazerowie();
    void laduj();
};
#endif
