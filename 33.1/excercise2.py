# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
lista_media = list(range(1, 11, 2))
print(lista_media)


def media_aritimetica(lista):
    soma_total = 0
    for numero in lista:
        soma_total += numero

    return soma_total / len(lista)


media = media_aritimetica(lista_media)
print(media)
