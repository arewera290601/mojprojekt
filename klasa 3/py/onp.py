
class Stos: 
    def __init__(self, maks=20):
        self.elementy = []
        self.maks = maks
        self.ostatni = 0
         
    def push(self, el):
        if self.ostatni >= self.maks:
            print("Stos pełny!")
            return False
        self.elementy.append(el)
        self.ostatni +=1
        return True
        
    def pop(self):
        if self.ostatni < 1:
            print("Stos pusty!")
            return False
        self.ostatni -= 1
        return self.elementy.pop()
        
class ONPKlasa(Stos):
    def __init__(self, o_str=''):
        super().__init__()
        self.o_str = o_str.strip()
        self.wynik = None
        
    def oblicz_onp(self):
        onp = self.o_str.split(" ")
        for wyraz in onp:
            if wyraz.isdigit():
                self.push(wyraz)
            else: 
                a = self.pop()
                b = self.pop()
                self.push(eval(str(b) + wyraz + str(a)))
        self.wynik = self.pop()


def main(args):
    
    w = input('Podaj wyrażenie:')
    onp = ONPKlasa(w)
    onp.oblicz_onp()
    print(onp.wynik)

    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
