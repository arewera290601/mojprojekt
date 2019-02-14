/* 
 * szyfr_Cezara.cpp
 * 
 * 
 */

#include <string.h>
#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(int klucz, char tab[])
{
	int dl = strlen(tab); //określenie ilości znaków wyrazu
	
	//sprawdzenie, czy klucz miesci sie w zakresie
	if(!(klucz >= -26 && klucz <= 26)) return;
	
	if(klucz >= 0)
		for(int i=0;i<dl;i++)
		if(tab[i] + klucz <= 'z')
			tab[i] += klucz;
		else
			tab[i] = tab[i] + klucz - 26; 
	else
		for(int i=0;i<dl;i++)
		if(tab[i] + klucz >= 'a')
			tab[i] += klucz;
		else
			tab[i] = tab[i] + klucz + 26;
}

int main(int argc, char **argv)
{
    
    int klucz = 0;
    char tab[MAKS];
    cout << "Podaj tekst:\n";
    cin.getline(tab, MAKS);
	cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(klucz, tab);
  
	return 0;
}

