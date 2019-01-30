/*
 * nieparzyste.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    
    for (int i = 1; i+2; i++){
        if(i == n)
            cout << n;
        else cout << i;
        }
        
        
	return 0;
}

