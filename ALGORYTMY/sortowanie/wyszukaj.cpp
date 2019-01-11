/*
 * szukaj.cpp
 * 
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int rozmiar) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for(int i=0; i < rozmiar; i++) {
        // cout << rand() << endl;
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar) {
    for(int i=0; i < rozmiar; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void sort_insert(int tab[], int n) {
   int i, k, el;
   for (i = 1; i < n ; i++){
       el = tab[i];
       k = i-1; // indeks porównywanegoelementu z częsci posortowanego elementu
       while (k >= 0 && tab[k]>el){
           tab[k+1]=tab[k];
           k--;
           }
           tab[k+1] = el;
        } 
    }

int szukaj_lin(int tab[], int n, int szuk) {
    for(int i = 0; i < n; i++)
        if (tab[i] == szuk)
            return i;
    return -1;
    
    }
// algorytm dziel i zwyciężaj- dzielić każda część na pół az zostanie jeden element

int szukaj_bin_lin(int tab[], int n, int szuk){
    int p, k, s, w;
    p = 0; k = n - 1; w = -1;
    while ( p <= k) {
        s = (p + k) / 2;
        if (tab[s] == szuk) {
            w = s;
            break;
        } else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
        }
        return w;
    }
    
int szukaj_bin_rek(int tab[], int szuk, int p, int k){
    if(p <= k){
        int s = (p + k) /2;
        if (tab[s] == szuk) return s;
        if (szuk < tab[s]) 
            return szukaj_bin_rek(tab, szuk, p, s-1);
        else 
            return szukaj_bin_rek(tab, szuk, s+1, k);
        }
    return -1;
    }
    
int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij(tab, n);
    drukuj(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: "; cin >> szuk;
    //~int indeks = szukaj_lin(tab, n, szuk);
	//~if (indeks != -1)
        //~cout << "Znaleziono!";
    //~else
        //~cout << "Nie znaleziono!";
    sort_insert(tab, n);
    int indeks = szukaj_bin_lin(tab, n, szuk);
    // int indeks = szukaj_bin_rek(tab, szuk, 0, n-1);
    if (indeks >= 0) cout << "Znaleziono: " << indeks << endl;
    else cout << "Nie znaleziono";
    return 0;
}

