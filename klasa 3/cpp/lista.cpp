/*
 * lista.cpp
 * 
 */


#include <iostream>
#include "lista.h"

using namespace std;

Lista::Lista(){
    header.head = NULL;
    header.tail = NULL;
}

Lista::~Lista(){
    while(header.head != NULL)
        Usun();
}

void Lista::Dodaj(int value){
    ELEMENT *el = new ELEMENT;
    el->value = value;
    el->next = NULL;
    if (header.head == NULL) {
        header.head = el;
        header.tail = el;
    } else {
        header.tail->next = el;
        header.tail = el;
    }
}

void Lista::Wyswietl(){
    ELEMENT *el = header.head;
    while (el != NULL) {
        cout << el->value << endl;
        el = el->next;
    }
}

int Lista::Usun() {
    if (header.head == NULL)
        return 0;
    int tmp;
    if (header.head == header.tail) {
        tmp = header.head->value;
        delete header.head;
        header.head = header.tail = NULL;
    } else {
        // tmp = header.tail->value;
        ELEMENT *el = header.head;
        while(el->next != header.tail)
            el = el->next;
        tmp = el->next->value; // 52=56
        delete el->next; // usuwamy ostatni element
        el->next = NULL;
        header.tail = el;
    }
    return tmp;
}

bool Lista::Pusta() {
    return header.head == NULL;
}
