def saludar(nombre_persona):
    """
    Recibe un nombre y muestra un saludo personalizado.
    No retorna nada (retorna None por defecto).
    """
    mensaje = f"¡Hola, {nombre_persona}! ¡Qué bueno tenerte aquí!"
    print(mensaje)

# ===== Uso directo de la función =====
saludar("Jimmy")

# ===== Nota sobre assert =====
# Como la función no devuelve valor, no es posible hacer pruebas con assert directamente.
# Pero podríamos modificarla para pruebas (ya lo veremos más adelante).
print("--- Fin del programa --- Jim Requena")