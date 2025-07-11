# Crear una lista con notas numéricas
mis_notas = [85.5, 90, 78, 88.5, 95, 82]

# Inicializar variable para la suma
suma_total = 0

# Usar bucle for para calcular la suma total sin usar sum()
for nota in mis_notas:
    suma_total += nota

# Calcular el promedio
promedio = suma_total / len(mis_notas)

# Imprimir resultados de forma clara
print(f"Suma total de las notas: {suma_total}")
print(f"Promedio de las notas: {promedio:.2f}")

# ----------------------------
# Validación con pruebas assert
# ----------------------------

# Cálculo esperado usando sum() como referencia
suma_esperada = sum(mis_notas)
promedio_esperado = suma_esperada / len(mis_notas)

# Pruebas
assert suma_total == suma_esperada, f"❌ Error: la suma debería ser {suma_esperada}"
assert promedio == promedio_esperado, f"❌ Error: el promedio debería ser {promedio_esperado:.2f}"

print("OK ¡Todo correcto! Las validaciones pasaron exitosamente.")
