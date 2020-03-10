/*
 * drzewo_bin.cpp
 * 
 */


#include <iostream>
using namespace std;

struct WEZEL {
        int wartosc;
        WEZEL* lewy;
        WEZEL* prawy;
} *korzen = NULL;

WEZEL* stworzWezel(int wartosc) {
        WEZEL* nowyWezel = new WEZEL;
        nowyWezel->wartosc = wartosc;
        nowyWezel->lewy = NULL;
        nowyWezel->prawy = NULL;
        return nowyWezel;
}

void dodajWezel(WEZEL* wezel, int wartosc) {
        if (korzen == NULL) {
                korzen = stworzWezel(wartosc);
        } else {
                if (wartosc < wezel->wartosc) { // wstawiamy do lewego poddrzewa
                        if (wezel->lewy != NULL) {
                                dodajWezel(wezel->lewy, wartosc);
                        } else {
                                wezel -> lewy = stworzWezel(wartosc);
                        }
                } else {
                        if (wezel->prawy != NULL) {
                                dodajWezel(wezel->prawy, wartosc);
                        } else {
                                wezel -> prawy = stworzWezel(wartosc);
                                }
                }
        }

}

void wyswietlRosnaco(WEZEL *wezel) {
        if (wezel !=NULL) {
                // rekurencyjnie wyswietlanie lewego poddrzewa
                wyswietlRosnaco(wezel->lewy);
                cout << wezel -> wartosc << ", ";
                // rekurencyjne wyswietlanie prawego poddrzewa
                wyswietlRosnaco(wezel->prawy);
        }
}

void wyswietlMalejaco(WEZEL *wezel) {
        if (wezel !=NULL) {
                // rekurencyjnie wyswietlanie prawego poddrzewa
                wyswietlMalejaco(wezel->prawy);
                cout << wezel -> wartosc << ", ";
                // rekurencyjne wyswietlanie lewego poddrzewa
                wyswietlMalejaco(wezel->lewy);
        }
}

void usunWezel(WEZEL* wezel, int wartosc) {
        
}

int main(int argc, char **argv)
{
        dodajWezel(korzen, 8);
        dodajWezel(korzen, 10);
        dodajWezel(korzen, 3);
        dodajWezel(korzen, 55);
        dodajWezel(korzen, 77);
        dodajWezel(korzen, 2);
        dodajWezel(korzen, 4);
        cout << "Drzewo posortowane malejąco:" << endl;
        //wyswietlRosnaco(korzen);
        wyswietlMalejaco(korzen);
	return 0;
}

