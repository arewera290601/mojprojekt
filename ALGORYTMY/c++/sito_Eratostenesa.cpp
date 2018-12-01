/*
 * sito_Eratostenesa.cpp
 * Eukides
 * Heron
 * Eratostenes
 * Fibonacci
 */


#include <iostream>
#include <cmath>
using namespace std;



int main(int argc, char **argv)
{
	int i, j, zakres, b;
    bool tab[100];
    cout << "Podaj górny zakres, max 99" << endl;
    cin >> zakres;
    b = sqrt((float)zakres);
    
    //inicjacja tablicy
    for(i = 2; i < zakres + 1; i++)
        tab[i] = true;
        
    for (i=2; i <= b; i++){
        if(tab[i] != false)
             for(j = i + i; j <= zakres + 1; j += i)
                tab[j] = false;
    }
    for (int i = 2; i <= zakres + 1; i++){
        if(tab[i] == true)
            cout << i << " ";
    }
	return 0;
}

