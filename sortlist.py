class sortlist(list):
    def __init__(self,lst):
        super().__init__(sorted(lst))
    def append(self,x):
        super().append(x)
        self.sort()

lista = sortlist([2,56,27,18])
print(lista)
lista.append(42)
print(lista)
print(lista.pop())
