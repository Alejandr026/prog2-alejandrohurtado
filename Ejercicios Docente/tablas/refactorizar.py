   # Refactorizar el código de la tabla de multiplicar
        # Autor: Fabrizzio Lora (FaXx0)
# Función para calcular áreas de rectángulos
def calcular_area_rectangulo(base, altura):
    return base * altura
    # Fin de la función
# Función principal con indentación FIXED
def mostrar_area_rectangulo(numero, base, altura): # Función principal
    area = calcular_area_rectangulo(base, altura)  #o area = base * altura
        # Fin de la función
    print(f"El área del rectángulo {numero} ({base}x{altura}) es: {area}") # Salida de datos
    # Fin de la función

# Rectángulos

# Rectángulo 1 (usando la función) # Llamada a la función principal con los parámetros correspondientes
mostrar_area_rectangulo(1, 10, 5)
# Rectángulo 2 (usando la función) # Llamada a la función principal con los parámetros correspondientes
mostrar_area_rectangulo(2, 7, 3)
# Rectángulo 3 (usando la función) # Llamada a la función principal con los parámetros correspondientes
mostrar_area_rectangulo(3, 15, 8)
    # Fin del programa