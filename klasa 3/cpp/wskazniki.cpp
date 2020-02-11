/*
 * wskazniki.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int x = 11;
        cout << "Wartość x: " << x << endl;
        cout << "Adres x: " << &x << endl;
        cout << "Wartość pod adresem: " << * &x << endl;
        cout << "Rozmiar x: " << sizeof(x) << endl;
        
        int *px = NULL;
        px = &x;
        cout << "Wartość wskaźnika: " << px << endl;
	cout << "Warość pamięci wskazywanej przez wskaźnik: " << *px << endl;
        *px = 20;
        cout << *px << endl;
        return 0;
}

