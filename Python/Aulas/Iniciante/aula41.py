# Aula de OR
# Or = Uma expressão verdadeira = tudo verdadeiro
entrada = input('E = entrar ou S = sair:')
print(entrada)
senha = input('Senha: ')

valor_senha = '1234'
# if condição == True
if (entrada == 'E' or entrada == 'e') and senha == valor_senha:
    print('Entrar')

else:
    print('Sair')

# Alaviação de curto circuito
# print(True and False and True)
senha = input('Senha: ') or 'Sem senha'
print(senha)
