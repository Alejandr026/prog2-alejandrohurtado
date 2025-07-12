lis_secret = [7, 12, 3, 21, 9]

print("Bienvenidos al Ahoracado")
print("Debes descubrir que numeros hay en la lista secreta de 5 elementos")
print("Pero no puedes verla directamente. En cada turno puedes hacer una \"Pregunta\" en forma de codigo Python")
print("Ejemplos: len(lis_secret), lis_secret[2], lis_secret[0] > 10")
print("Cuando creas tener la lista completa escribe Adivinar")
print("--------------------------------------------------------------------------------------------------------------")

while True:
    instruccion = input("Escribe tu instruccion o adivinar")
    if instruccion.strip().lower() == "adivinar":
        intento = input("Escribe tu intento de lista (separada por comas):")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lis_secret:
                    print("Correcto, descubriste la lista secreta.")
                    break
            else:
                 print("Esa no es la lista correcta. Sigue preguntando")
        except ValueError:
             print("Error segurate de escribir solo numeros separados por comas")
    else:
         try:
              resultado = eval(instruccion, {"lis_secret" : lis_secret})
              print("Resultado: ", resultado)
         except Exception as e:
                print("Error en tu instruccion", e)
              
