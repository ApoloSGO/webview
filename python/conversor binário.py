class Pilhas:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        if len(self.data) > 0:
            return self.data.top(-1)

    def empty(self):
        return not len(self.data) > 0


p = Pilhas()
num = int(input("insira um numero: "))
while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

numero = []
while not p.empty():
    numero.append(p.pop())

sequencia = ".".join(map(str, numero))
print("sequencia de Numeros:", sequencia)
