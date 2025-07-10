def verificar_adivinanza(numero_secreto, intento):
    """Devuelve una pista según la diferencia entre el intento y el número secreto."""
    if intento < numero_secreto:
        return "Demasiado bajo"
    elif intento > numero_secreto:
        return "Demasiado alto"
    else:
        return "Correcto"

# ====== Pruebas unitarias ======
assert verificar_adivinanza(7, 3) == "Demasiado bajo", "Error: se esperaba 'Demasiado bajo'"
assert verificar_adivinanza(7, 10) == "Demasiado alto", "Error: se esperaba 'Demasiado alto'"
assert verificar_adivinanza(7, 7) == "Correcto", "Error: se esperaba 'Correcto'"

print("✅ Pruebas unitarias superadas.")

# ====== Juego interactivo ======
numero_secreto = 7
print("🔐 Adivina el número secreto entre 1 y 10.")

while True:
    try:
        intento = int(input("Ingresa tu número: "))
        resultado = verificar_adivinanza(numero_secreto, intento)

        if resultado == "Correcto":
            print(f"🎉 ¡Correcto! El número era {numero_secreto}.")
            break
        else:
            print(f"❌ {resultado}. Intenta de nuevo.")
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
