/*
 * szyfr_przestawieniowy.cpp 
 */

#include<iostream>
#include<cstring>
using namespace std;

void kodowanie(char *napis)
{
	int dl = strlen(napis); //wyznaczenie liczby znaków
	
	for(int i=0; i<dl-1; i+=2) //przesuwamy się o dwa znaki
	//zamiana sąsiadujących znaków
	{
		char pom = napis[i];
		napis[i] = napis[i+1]; //dlatego w pętli i<dl-1
		napis[i+1] = pom;	
	}
}

int main()
{
	char napis[100];
	
	cout<<"Podaj napis do zaszyfrowania: ";
	cin.getline(napis, 100);
	//szyfrujemy
	kodowanie(napis);
	cout<<"Szyfrogram: ";
	cout<<napis<<endl;
	
	
	cin.get();
	return 0;
}
