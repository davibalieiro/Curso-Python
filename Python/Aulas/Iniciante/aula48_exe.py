nome = input('Digite seu nome: ')
idade = input('Digite seu idade: ')
if nome and idade:
    print(f'Você tem {idade} de idade')
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido fica {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaços')
    # nome_len = len(nome)
    # print(f'Seu nome tem {nome_len} letras')
    print(f'Seu tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpa, você é uma mula e nao degitou nada')
