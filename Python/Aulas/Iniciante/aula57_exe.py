nome = input('Digite seu primeiro nome: ')
print(f'Seu nome {nome}')
letras = len(nome)
if letras > 1:
    if letras <= 4:
        print('Seu nome é curto')
    elif letras >= 5 and letras <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Por favor digite mais de uma letra')
