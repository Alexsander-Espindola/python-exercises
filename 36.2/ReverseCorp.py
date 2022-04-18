def ReverseCorp(list):
    tamanho = len(list)
    for i in range(tamanho//2):
        seguraAi = list[tamanho - i - 1]
        seguraDnv = list[i]
        list[tamanho - i - 1] = seguraDnv
        list[i] = seguraAi

    return list


list = ["a", "c", "d", "b", "f", "e", "g"]
print(ReverseCorp(list))
