# Funcções decaradoras
# Decorar = Adicionar Remover Restringir Alterar
# São funções que decorar outras funções
# Usar em Python
# O Python tem um açucar Sintatico @sytax_sugar


def criar(funcao):
    def interna(*args, **kargs):
        for i in args:
            e_string(i)
        resultado = funcao(*args, **kargs)
        return resultado

    return interna


@criar
def inverter(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Paramentro deve ser srtings')


inverter_chegando = criar(inverter)


inver = inverter('Davi')
print(inver)
