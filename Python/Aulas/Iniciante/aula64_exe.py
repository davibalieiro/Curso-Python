# Iterando strings co while
'''
nome = 'Davi Balieiro'
tam_nome = len(nome)
print(nome)
print(tam_nome)

nova_string += "*D*"
'''
nome = 'Cristiano Ronaldo'
n1 = 0
novo = ''
while n1 < len(nome):
    letra = (nome[n1])
    novo += f'*{letra}'
    n1 += 1
novo += f'*'
print(novo)
