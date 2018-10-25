#include <iostream>
#include <cstdlib>

using namespace std;
void minmax(){
    char dalej = 't';
    int liczba = 0;
    int min, max;
    cout << "Podaj liczbę: ";
    cin >> liczba;
    min = max = liczba;
    while(dalej == 't'){
        cout << "Podaj liczbę: ";
        cin >> liczba;
        if (liczba < min)
            min = liczba;
        if (liczba > max)
            max = liczba;
        cout << "Nastepna (t/n)?";
        cin >> dalej;
    }
    cout << "Najmniejsza: " << min << endl;
    cout << "Największa: " << max << endl;
}

void wypelnij(int tab[], int rozmiar) {
cout << "Podaj " << rozmiar << " liczb: " << endl;
    for(int i=0; i < rozmiar; i++) {
        cin >> tab[i];
    }
}

void wypelnij_los(int tab[], int rozmiar) {
    srand(time(NULL)); // inicjqacja generatora liczb pseudolosowych
    for(int i=0; i < rozmiar; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar) {
    for(int i=0; i < rozmiar; i++) {
        cout << tab[i] << " ";
    }
}


int main()
{
    int rozmiar = 50;
    int tab[rozmiar];
    wypelnij_los(tab, rozmiar);
    drukuj(tab, rozmiar);
   // minmax();
    return 0;
}
