faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f'Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}') # o "f" serve pra poder manipular o texto dentro do parenteses, usando {}
nome = 'joão Paulo'
email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find('@')) # find = indice numérico do texto

posicao = email.find('@')
servidor = email[posicao:]
posicao = nome.find(' ')
primeiro_nome = nome[ :posicao] # os 2 pontos ,":", antes do indice conta redigita até o numero do índice, sem incluílo
print(primeiro_nome)
print(servidor)
tamanho = len(email) #len() usado pra ver o tamanho do texto
print(tamanho)

email_trocado = email.replace('gmail.com', 'hotmail.com') # troca de texto usando replace()
print(email_trocado)

margem = lucro / faturamento
print(f' faturamento: R${faturamento:,.2f}\n Custo:R${custo:,.2f}\n Lucro:R${lucro:,.2f}') #editando com caracteres especiais :,.2f}\n
print(f'margem:{margem:.1%}')

#.lower() serve para deixar o texto em letra minúscula

total_imposto = 0
dic_precos = {"celular":1500,"camera":1000,"fone de ouvido":800,"monitor":2000} #exemplo de uso do dicionario pra formar listas compostas por valores em cada item
produto_procurado = input("Digite um produto:")
produto_procurado = produto_procurado.lower()
if  produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"produto: {produto_procurado},Preço:{preco}")
else:
    print("produto não encontra, tente novamente")

valor_total_produtos = sum(dic_precos.values())   #sum(****.values()) usado pra contar os valores de uma lista
print(valor_total_produtos)


vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}


#saber quanto variou percentualmente cada mes de 2023 em comparação com 2022
faturamento_total_simulado = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual= valor_23/valor_22 - 1
    if valor_23 < valor_22:
        faturamento_total_simulado = faturamento_total_simulado + valor_22
    else:
        faturamento_total_simulado = faturamento_total_simulado + valor_23
    print(f"variação do {mes}: {var_percentual:.1%}")  

print(faturamento_total_simulado)
    

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual= valor_23/valor_22 - 1
    if valor_23 < valor_22:
        vendas_23[mes] =valor_22

faturamento_total = sum(vendas_23.values())
print(faturamento_total_simulado)
semestre = len(vendas_23) # quantidade de itens em uma lista
print(semestre)
# Lista de exemplo
lista = [1, 2, 3, 4, 1, 2, 1, 1]

# Contando todos os itens únicos
contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

print("Contagem de itens únicos na lista:", contagem)
