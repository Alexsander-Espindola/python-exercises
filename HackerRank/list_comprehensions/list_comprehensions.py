def funcao_filtra(lista):
    return sum(lista) != n

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lista = [[i, j, k] for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)]
    
    lista = list(filter(funcao_filtra, lista))
    
    print(lista)
    