# Exemplo de uso de stes

letras = set()
while True:
    letra = input('Digite uma letra:')
    letras.add(letra)

    if 'd' in letras:
        print('Parabens')
        break
    print(letras)
