def sumar(a, b):
    """
    Recibe dos números y devuelve su suma.
    """
    resultado_suma = a + b
    return resultado_suma

# ===== Pruebas unitarias con assert =====
assert sumar(2, 3) == 5, "Error: 2 + 3 debe ser 5"
assert sumar(-1, 1) == 0, "Error: -1 + 1 debe ser 0"
assert sumar(10, 0) == 10, "Error: 10 + 0 debe ser 10"

print("✅ Pruebas unitarias para sumar() superadas.")
