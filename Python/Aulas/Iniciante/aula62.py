# Aula de while
# loop infinito = Quando o codigo nao tem fim

i = 1
while i <= 100:
    i += 1
    print(i)
    if i == 10:
        print('Nao vou mostra o 10')
        continue
    if i >= 11 and i <= 30:
        #        print('Nao vou mostra do ',i)
        continue

    if i == 50:
        break
print('Acabou')
