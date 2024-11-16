n1 = input('Digite um numero inteiro: ')

if n1.isdigit():
    n2 = int(n1)
    decisao = n2 % 2 == 0
    opcao = 'impar'
    if decisao is True:
        opcao = 'par'
    print(f'O numero {n2} é {opcao}')

else:
    print('Voce nao digitou um numero inteiro')
