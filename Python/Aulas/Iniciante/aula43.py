# Aula de in e in not
# Strings são iteráveis
#  0 1 2 3
#  D A V I
# -4-3-2-1

nome = 'Davi'
# print(nome[3])
print('D' in nome)
print('F' in nome)
print(10 * '-')
print('D' not in nome)
print('F' not in nome)


pessoa = input('Digite seu nome: ')
buscar = input('O que deseja buscar: ')

if buscar in nome:
    print(f'{buscar} esta em {nome}')

else:
    print(f'{buscar} não esta em {nome}')
