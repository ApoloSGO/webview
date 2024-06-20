class Fila():
    def __init__(self):
        self.data = []
        
    def inserir(self,x):
        self.data.append(x)
    
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            return None
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    def __str__(self):
        if self.data:
            return "^".join(map(str,self.data))
        else:
            return "Fila vazia"
    



fila = Fila()

fila_Prioridade = Fila()

proximo_prioridadde = fila_Prioridade.remover()
while True: 
    entrada = input("Insira sua idade (ou 'sair' para terminar):")

    if entrada.lower() == "sair":
        break
    try:
        idade = int(entrada)
        if idade >60:
            fila_Prioridade.inserir(idade)
            print(fila_Prioridade)
        
        else:
            fila.inserir(idade)
            print(fila)
        
    except ValueError:
        print("por favor, insira um numero valido.")



class Pilha(): 
    def __init__(self): 
        self.data = [ ] 
 
    def push(self, x): 
        self.data.append(x) 
 
    def pop(self): 
        if len(self.data) > 0: 
            return self.data.pop(-1) 
 
    def empty(self): 
        return len(self.data) > 0 
 
p = Pilha() 
q = Pilha() 
for i in range(5): 
    if i % 2 == 0: 
        p.push(i) 
    else: 
        q.push(i) 
while p.empty(): 
    q.push(p.pop()) 
while q.empty(): 
    print(q.pop()) 
