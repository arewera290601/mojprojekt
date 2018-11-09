/*
 * anagramy.cpp
 * 
 */


#include <iostream>

using namespace std;


int main(int argc, char **argv)
{
	char wyraz[] = "ryba";
    int roz = 4;
    int i1, i2, i3, i4;
    i1 = i2 = i3 = i4 = 0;
    // 0123
    for (i1 = 0; i1 < roz; i1++){
         for (i2 = 0; i2 < roz; i2++){
            if (i1 == i2) continue;
            for (i3 = 0; i3 < roz; i3++){
                    if (i1 == i3 || i2 == i3) continue;
                    i4 = 6 - i1 - i2 -i3;
                    cout << wyraz[i1] << wyraz[i2] 
                    << wyraz[i3] << wyraz[i4] << endl;
                            
                 }
             //cout << i1 << i2 << endl;
             }
        }
	return 0;
}

