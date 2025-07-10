mis_notas = [10, 10, 10, 10, 10]
sum_total = 0
for i in mis_notas:
    sum_total = sum_total + i

promedio = sum_total / len(mis_notas)
print(f"La suma total de todas las notas es de: {sum_total}")
print(f"El promedio de las notas es de: {promedio}")