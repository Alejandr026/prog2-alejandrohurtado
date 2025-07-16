# Diccionario de colores
pixel = {
    0: "⬜",  # Blanco
    1: "⬛",  # Negros
    2: "🟩"   # Verde
}

# Diseño de la matris (no se me ocurrio una mejor manera xD)
alien = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
    [0,0,0,1,2,1,0,0,0,1,2,1,0,0,0],
    [0,0,0,1,1,2,1,1,1,2,1,1,0,0,0],
    [0,0,0,1,2,2,2,2,2,2,2,1,0,0,0],
    [0,0,1,2,2,1,2,2,2,1,2,2,1,0,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [0,1,2,1,2,2,2,2,2,2,2,1,2,1,0],
    [0,1,2,1,2,1,1,1,1,1,2,1,2,1,0],
    [0,1,1,0,1,2,2,1,2,2,1,0,1,1,0],
    [0,0,0,0,0,1,1,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
]

# Función para mostrar el dibujo
def mostrar_matriz(matriz):
    for fila in matriz:
        print("".join(pixel[val] for val in fila))

mostrar_matriz(alien)
