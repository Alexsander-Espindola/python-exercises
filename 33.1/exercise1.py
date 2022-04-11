# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "Os dois números são iguais"


resultado_x_igual_y = maior_numero(13, 13)
resultado_x_maior_y = maior_numero(13, 11)
resultado_y_maior_x = maior_numero(11, 16)

print(resultado_x_igual_y, resultado_x_maior_y, resultado_y_maior_x)
