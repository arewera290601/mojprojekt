/*
 * znaki.cxx
 */



#include <iostream>

using namespace std;

void licz_znaki(char tb[], int roz) {
    //~for(int i=0; i < roz; i++) {
       //~cout << tb[i];
    //~}
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
    cout << "Duże litery: " << literyD << endl; 
    cout << "Małe litery: " << literyM << endl; 
    cout << "Cyfry: " << cyfry << endl;
    cout << "Reszta: " << reszta << endl; 
}


int main(int argc, char **argv)
{
    const int rozmiar = 20;
	char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, cin.gcount());
	return 0;
}

