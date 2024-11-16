# Aula de Repetição
# while (enquanto)
# Executa uma ação enquanto uma condiçãofor verdadeira

valor = True
while valor:
    nome = input('Qual o seu nome ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou')
