def sumar_elementos(list_num):
    sum = 0
    for i in list_num:
        sum = sum + i
    return sum

lista = [10, 10, 10]
total = sumar_elementos(lista)
print(total)