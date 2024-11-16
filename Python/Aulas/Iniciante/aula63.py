linhas = 3
colunas = 3

linha = 1
coluna2 = 1
while linha <= linhas:
    coluna2 = 1
    while coluna2 <= colunas:
        print(f'{linha=} {coluna2=}')
        coluna2 += 1
    linha += 1


print('Acabou')
