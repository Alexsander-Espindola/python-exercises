def array_diff(list_a, list_b):
    list_c = []
    for i in list_a:
        if i not in list_b:
            list_c.append(i)

    return list_c
