
def parametros_decorador(name):
    def decorador(func):
        print('trem')

        def sua_new_func(*args, **Kwargs):
            res = func(*args, **Kwargs)
            final = f'{res} {name}'
            return final
        return sua_new_func
    return decorador


@parametros_decorador(name='Suiii')
def soma(x, y):
    return x+y


valor = soma(10, 5)
print(valor)
