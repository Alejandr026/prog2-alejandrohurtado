texto = "hola"
invertido = ''.join(texto[i] for i in range(len(texto) - 1, -1, -1))
print(invertido)  # Resultado: "aloh"
