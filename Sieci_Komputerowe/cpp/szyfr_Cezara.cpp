/*
 * szyfr_cezara.cpp 
 */

using namespace std;

#include <iostream>
#include <string.h>
#define MAKS 100

void szyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tb[i] != '\0'){
        kod = (int)tb[i] + klucz;
        if (tb[i] == ' '){
            kod -= klucz;
        } else if (kod > 122){
            kod -= 26;
        }
        cout << (char)kod;
        tb[i]= (char)kod;
        i++;
    }
    cout << endl;
}

int main(int argc, char **argv)
{
	char tekst[MAKS];
    int klucz = 0;
    
    cout << "Podaj tekst w małych literach: " << endl;
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);
	return 0;
}
