/*
 * figury.cpp
 * 
 */


#include <iostream>

using namespace std;

int prostokat2(a, b, znak){
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if (j == 0 && j == b - 1 && i == 0 && i == a - 1){
                    }
    
}


int main(int argc, char **argv)
{
    int a, b; // deklaracja
    a = b = 0; // inicjacja
    //int a = 0; // definicja
    cout << "Podaj bok 1: ";  
    cin >> a;
    cout << "Podaj bok 2: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokąt2(a, b, znak);
	return 0;
}

