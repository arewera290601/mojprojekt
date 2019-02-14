/* 
 * szyfr_Cezara.cpp
 * 
 * 
 */

#include <iostream>

using namespace std;

int main()
{
  char t[256];
  int i,w;

  cin >> w;              // odczytujemy rodzaj pracy programu

  cin.ignore(255,'\n');  // usuwamy pozostawiony w strumieniu znak \n

  cin.getline(t,256);    // odczytujemy tekst

  for(i = 0; t[i]; i++)  // przeglądamy kolejne znaki
    if(t[i] >= 'A' && t[i] <= 'Z')
    {
       if(w) t[i] = 65 + (t[i] - 42) % 26;
       else  t[i] = 65 + (t[i] - 62) % 26;
    } 

  cout << t << endl;     // wyświetlamy przetworzony tekst

  return 0;
} 

