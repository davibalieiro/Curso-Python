'''
Cuidados com dados mutaveis
= - copiando o valor(imutaveis)
= - apnta para o mesmo valor na memoria

'''
lista_a = ['Davi', 'Cristiano', 1, True]
lista_b = lista_a.copy()


lista_a[0] = 'Suiiiii'

print(lista_a)
print(lista_b)
