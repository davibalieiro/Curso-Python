horario = input('Digite a hora do dia: ')
print(horario)
if horario.isdigit():
    hora = int(horario)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Nao conheco essa hora')
else:
    print('Por favor, digite um numero inteiro')
