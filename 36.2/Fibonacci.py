def fibonacci(n):
    list = [0, 1]
    for i in range(1, n):
        nextNumber = list[i - 1] + list[i]
        list.append(nextNumber)
    return list


print(fibonacci(10))
