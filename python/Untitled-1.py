

def media(Nota_N1,Nota_N2):
    Resultado = (0.4 * Nota_N1 + 0.6 * Nota_N2)
    return Resultado

Nota_N1 = float(input('digite nota da prova:'))
Nota_N2 = float(input('digite nota das atividades:'))

Media = media(Nota_N1,Nota_N2)

if 5>Media:
    print('Reprovado')

else:
    print('Aprovado')

print(Media)
    

        