# Objetivo é descobrir qual letra apareceu mais vezes
frase = 'O Python é uma linguagem de programação'\
    'multiparadigma'\
    'o Python foi criado po Guido van Rossum.'

i = 0
apareceu = 0
apareceu_letras = ''
while i < len(frase):
    letra = frase[i]
    i += 1
    if letra == ' ':
        continue
    letras_imprimidas = frase.count(letra)

    if apareceu <= letras_imprimidas:
        apareceu = letras_imprimidas
        apareceu_letras = letra


print(
    'A letra que apareceu mais vezes foi '
    f'"{apareceu_letras}" que apareceu '
    f'{apareceu}x'
)
