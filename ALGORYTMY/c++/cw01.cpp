/*
 * cw01.cpp
 * 
 * 
 */


#include <iostream>
#include <iomanip>
using namespace std;

int cw01(){
    int suma = 0;
    for(int i=10; i <= 99; i++){
        if(i % 2==0)
        suma += suma + i;
    }
    cout << "Suma: " << suma << endl;
}

void cw02(){
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    
    while(a+b!=c) {
        a=b;
        b=c;
        cin >> c;
        }
    cout << c;
    }
    
    
int main(int argc, char **argv)
{
    cw01();
    cw02();
}


