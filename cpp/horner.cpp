/*
 * horner.cpp
 * W(x) = 2 x^3 + 3x^2 + 5x + 4 => 6
 * W(x) = x(2x^2 + 3x + 5) + 4 
 * w(x) = x(x(2x+ 3) + 5) + 4 => 3
 * 
 */

#include <iostream>
using namespace std;

void drukujw(int st, float tb[]){
    // 2x^3 + 3x^2 + 5x + 4 
    int i = 0;
    for(i = 0; i < st; i++) {
        cout << tb[i] << "x^" << st - i << " + ";
        }
    cout << tb[i];
    }


int main(int argc, char **argv)
{
    int stopien = 0;
    float *tbwsp; // wspaźnik typu rzeczywistego rozpoznać można po * (wspaxnik zawiera adres pamięci)
    float x =0;
	cout << "Stopień wielomianu: ";
    cin >> stopien;
    
    tbwsp = new float [stopien + 1];
    cout << tbwsp;
    
    for(int i=0; i <= stopien; i++){
        cout << "Podaj współczynnik przy najwyższej potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
        }
    
    cout << "Argument:  ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    
    
	return 0;
}

