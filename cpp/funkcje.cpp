/*
 * szablon.cpp
 * */

#include <iostream>

using namespace std;

int dodaj(int a, int b){
    return a + b;
    }
int dodaj2(int a, int b){
    return a - b;
    } 
int dodaj3(int a, int b){
    return a * b;
    }
int dodaj4(int a, int b){
    return a / b;
    }

int main(int argc, char **argv)
{
    
	float a, b; // deklaracja zmiennej
    a = b = 0; // inicjacja zmiennej 
    cout << "Podaj 1. liczbę: ";
    cin >> a; // zatrzyma wykonywanie probramu czeka aż użytkownik wprowadzi zmienna i kliknie enter
    cout << a << endl;  
    
    cout << "Podaj 2. liczbę: ";
    cin >> b;
    cout << b << endl;
    
    
    cout << "Suma: " << dodaj(a, b) << endl;
    cout << "Róźnica: " << dodaj2(a , b) << endl;
    cout << "Iloczyn: " << dodaj3(a, b) << endl;
    cout << "Iloraz: " << dodaj4(a, b) << endl;

	return 0;
}

