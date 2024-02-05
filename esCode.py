class Coda:
    def __init__(self):
        self.lista = []

    def is_empty(self):
        return len(self.lista) == 0

    def enqueue(self, a):
        self.lista.append(a)

    def dequeue(self):
        if self.is_empty():
            print("coda vuota")
        else:
            return self.lista.pop()
        return None
    
    def stampa(self):
        print(self.lista)

def main():
    coda = Coda()
    coda.enqueue(19)
    coda.enqueue(20)
    coda.dequeue()
    coda.stampa()

if __name__ == "__main__":
    main()