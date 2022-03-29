# Exercício 4: Crie uma função que receba uma lista
# de nomes e retorne o nome com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
# o retorno deve ser "Fernanda".

lista = [
    "José",
    "Lucas",
    "Nádia",
    "Fernanda",
    "Cairo",
    "Maria Clara Jucelina dos Santos Pereira Castro",
    "Joana",
]


def qual_maior_nome(lista_nomes):
    maior_nome = ""
    for nome in lista_nomes:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return maior_nome


print(qual_maior_nome(lista))
