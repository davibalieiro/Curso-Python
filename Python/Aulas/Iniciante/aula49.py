'''
Introdução ao try/except
try -tentar executar o código
except - ocorreu algum erro ao tentar executar
'''
n1 = input('Digite um numero para ser dobrado: ')
try:
    n1 = int(n1)
    print('INT:', n1)
    print(f'O dobro de {n1} é {n1 * 2}')
except:
    print('O que voce digitou nao é um numero')

# if n1.isdigit():
#    n1 = int(n1)
#    print(f'O dobro de {n1} é {n1 * 2}')
# else:
#    print('O que voce digitou nao é um numero')
