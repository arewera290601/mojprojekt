#ifndef _Stos_H_
#define _Stos_H_

#include "lista.h"

class Stos {
    private:
        Lista lista;
    public:
        void Push(int);
        int Pop();
        bool Pusty();
        
};
#endif 
