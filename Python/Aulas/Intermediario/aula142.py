lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for i in lista:
    if isinstance(i, set):
        i.add(5)
        print(i, isinstance(i, set))
