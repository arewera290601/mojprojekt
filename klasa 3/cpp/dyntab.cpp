/*
 * dyntab.cpp
 * 
 */


#include <iostream>
using namespace std;

void tabd_1() {
        float *tb = NULL;
        int ile;
        float liczba;
        
        cout << "Ile liczb podasz?" << endl;
        cin >> ile;
        
        try {
                tb = new float[ile];
        } catch(bad_alloc) {
                cout << "Za mało pamięci!";
                // return -1;
        }
        
        for (int i=0; i<ile; i++) {
                cout << "Podaj liczbę: ";
                cin >> liczba;
                cout << (tb+i) << endl;
                *(tb+i) = liczba;
        }
        delete [] tb; // zwolnienie pamięci
}

void tabd_2() {
        int w, k, i, j;
        srand(time(NULL));
        cout << "Podaj liczbę wierszy i kolumn tablicy: ";
        cin >> w >> k;
        int **tb; // deklaracja wskaźnika do wskaźnika
        try {
                tb = new int *[w]; // tworzenie tab. wskaźników
        } catch(bad_alloc) {
                cout << "Błąd!";
        }
        
        for (i=0; i<w; i++) {
                try{
                        tb[i] = new int[k];
                } catch(bad_alloc) {
                        cout << "Błąd!";
                }
        
        }
        for (i=0; i<w; i++) {
                for(j=0; j<k; j++) {
                        tb[i][j] = rand() % 101;
                        cout << setw(4) << tb[i][j];
                }
                cout << endl;
        }
        for (i=0; i<w; i++) {
                delete [] tb[i];
        }
        delete [] tb;
}

int main(int argc, char **argv)
{
	tabd_1();
	tabd_2();
	return 0;
}

