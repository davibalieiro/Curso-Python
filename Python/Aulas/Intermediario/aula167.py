def fabrica_de_decoradores(a=None, b=None, c=None):
    def decoradora(func):
        print('Decoradora 1')

        def anilhada(*args, **Kwargs):
            print('Aninhadas')
            res = func(*args, **Kwargs)
            return res
        return anilhada
    return decoradora


mult = fabrica_de_decoradores()(lambda x, y: x*y)


@fabrica_de_decoradores()
def soma(x, y):
    return x + y


valor = soma(5, 10)
print(valor)
print(mult)
