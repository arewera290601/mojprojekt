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

int min(int tab[], int rozmiar){
    int min = tab[0];
    for(int i=1; i < rozmiar; i++){
        if (tab[i] < min)
            min = tab[i];
        }
        return min;
}

int max(int tab[], int rozmiar){
    int max = tab[0];
    for(int i=1; i < rozmiar; i++){
        if (tab[i] > max)
            max = tab[i];
        }
        return max;
}

int main()
{
    int rozmiar = 50;
    int tab[rozmiar];
    wypelnij_los(tab, rozmiar);
    drukuj(tab, rozmiar);
    cout << "\n\nMin: " << min(tab, rozmiar) << endl;
    cout << "\n\nMax: " << max(tab, rozmiar) << endl;
   // minmax();
    return 0;
}
