def encontrar_mayor (list_num):
    if not list_num:
        return None
    mayor = list_num[0]

    for i in list_num:
        if mayor < i:
            mayor = i
    return(mayor)

lista = [1, 2, 3, 4, 5]
num_mayor = encontrar_mayor(lista)
print(num_mayor)
