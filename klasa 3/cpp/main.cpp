/*
 * main.cpp
 */


#include <iostream>
#include "lista.h"
#include "stos.h"

using namespace std;

int main(int argc, char **argv)
{
	Lista lista;
    lista.Dodaj(1);
    lista.Dodaj(2);
    lista.Dodaj(3);
    lista.Dodaj(4);
    lista.Dodaj(5);
    lista.Dodaj(6);
    lista.Dodaj(7);
    cout << lista.Usun() << endl;
    cout << lista.Usun() << endl;
    lista.Wyswietl();
    
    Stos stos;
    stos.Push(10);
    stos.Push(11);
    cout << stos.Pop() << endl;
    stos.Push(12);
    stos.Push(13);
    cout << stos.Pop() << endl;
	return 0;
}

