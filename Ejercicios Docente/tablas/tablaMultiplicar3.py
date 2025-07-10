def tabla_multiplicar(numero, hasta=10):
    """Devuelve una lista con la tabla de multiplicar de 'numero' hasta 'hasta'."""
    return [numero * i for i in range(1, hasta + 1)]

# ===== Pruebas unitarias =====
assert tabla_multiplicar(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], "Error en la tabla del 2"
assert tabla_multiplicar(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], "Error en la tabla del 5"
assert tabla_multiplicar(0) == [0] * 10, "Error en la tabla del 0"

print("✅ Pruebas unitarias pasadas con éxito.")

# ===== Ejecución interactiva =====
num_tabla = int(input("Introduce el número de la tabla: "))
print(f"--- Tabla del {num_tabla} ---")

for i, resultado in enumerate(tabla_multiplicar(num_tabla), start=1):
    print(f"{num_tabla} x {i} = {resultado}")

print("--- Fin del programa --- Jim Requena")
