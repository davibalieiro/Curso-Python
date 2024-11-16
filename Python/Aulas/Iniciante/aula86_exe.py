# Exiba os indices da lista
# Minha solução
lista = ['Davi', 'João', 'Augusto', 'Matheus', 'José']
i = -1
for nome in lista:
    print(i, '.', nome)
    i += 1

# Solução do Luíz
lista = ['Davi', 'João', 'Augusto', 'Matheus', 'José']
indeces = range(len(lista))

for i in indeces:
    print(i, lista[i])
