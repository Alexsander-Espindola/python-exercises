# Exercício 3: Faça um programa que,
# dado um valor n qualquer, tal que n > 1
# ,imprima na tela um quadrado feito de asteriscos de
# lado de tamanho n
# https://treinamento24.com/library/lecture/read/210894-como-juntar-uma-lista-de-string-python

n = 5


def faz_um_quadrado(n_de_lados):
    quadrado = []
    for j in range(n_de_lados):
        quadrado.append("*")
    for i in range(n_de_lados):
        print("".join(quadrado))


# Dica: Python sabe multiplicar sequências!
# Por exemplo, 3 * 'bla' resulta em blablabla .
# Isso se aplica a listas também, caso você precise.


def quadrado_com_dica(n_de_lados):
    linda_do_quadrado = n_de_lados * "*"
    for i in range(n_de_lados):
        print(linda_do_quadrado)


retorno = quadrado_com_dica(n)
retorno = faz_um_quadrado(n)
