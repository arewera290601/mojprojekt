/* 
 * szyfr_Cezara.cpp
 * 
 * 
 */

#include <string.h>
#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(char tekst, int klucz){
    int ilosc = 0;
    ilosc = strlen(tekst);
    
    int i = 0;
    int cyfry, literyD, literyM, reszta;
    cyfry = literyD = literyM = reszta = 0;
    int znak_kod = 0; //kod ASCII badanego znaku
    
    
    while(tb[i] != '\0'){
        znak_kod = (int)tb[i];
        if (znak_kod > 64 && znak_kod < 91) // to sprawia że sa duże litery
            literyD++;
        else if (znak_kod > 96 && znak_kod < 123)
            literyM++;
        else if (znak_kod > 47 && znak_kod < 58)
            cyfry++;
        else 
            reszta++;
        
    i++;  //inkrementcja indeksu
   }

    }

int main(int argc, char **argv)
{
    int klucz = 0;
    char tekst[MAKS];
    cout << "Podaj tekst:\n";
    cin.getline(tekst, MAKS);
	cout << "Podaj klucz: ";
    cin >> klucz;
     //~szyfruj(tekst, klucz);
  
	return 0;
}

