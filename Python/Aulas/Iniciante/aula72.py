# Aula de For/in = "para"
# O while é pra quando nao sei quantas vezes o repetir
# For eu sei
'''
texto = 'Python'
i = 0
tamanho = len(texto)
while i < tamanho:
    print(texto[i])
    i += 1
'''
'''
senha = '1234'
senha_digitada = ''
i = 0
while senha != senha_digitada:
    senha_digitada = input(f'Digite a senha({i})x: ')
    i += 1
print(i)
print('Acabou aqui')
'''
texto = 'Python'
ntexto = ''
for letra in texto:
    ntexto += f'*{letra}'
    print(letra)
print(f'{ntexto}*')
