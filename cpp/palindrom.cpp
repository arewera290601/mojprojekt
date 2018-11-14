/*
 * palindrom.cpp
 * 
 * 
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char w[], int r){
    bool pal = true;
    int polowa = r / 2;
    for(int i = 0; i < polowa; i++)
    {
        if (w[i] == w[r - 1 - i]) 
            ;
        else {
            pal = false;
            break;
            }
    }   
    return pal;
}

int main(int argc, char **argv)
{
	int roz = 20;
    char wyraz[roz];
    cout << "Podaj wyraz: ";
    cin.getline(wyraz, roz);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
	return 0;
}

