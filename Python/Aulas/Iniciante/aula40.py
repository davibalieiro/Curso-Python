# Aula de AND
# and/ or/ not
#   e/ ou/ não
# and = Todas as afirmações precisam ser verdadeiras
# None é usado para representar um não valor
entrada = input('E = entrar ou S = sair:')
print(entrada)
senha = input('Senha: ')

valor_senha = '1234'
# if condição == True
if entrada == 'E' and senha == valor_senha:
    print('Entrar')

else:
    print('Sair')

print(True and False and True)
