lista_tareas = []
proximo_id_tarea = 1

def agregar_tarea(descripcion, prioridad = "media"):
    global proximo_id_tarea
    nueva_tarea = {
        "id": proximo_id_tarea,
        "descripcion": descripcion,
        "completada": False,
        "prioridad": prioridad
    }
    lista_tareas.append(nueva_tarea)
    proximo_id_tarea += 1
    print(f"✅ Tarea '{descripcion}' añadida con éxito.")

def mostrar_tareas():
    print("\n--- 📝 LISTA DE TAREAS ---")
    if not lista_tareas:
        print("No hay tareas pendientes a viciar al WOW")
        return
    
    for tarea in lista_tareas:
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

"""print("==========================================")

agregar_tarea("Estudiar para el examen de Programacion 2")
agregar_tarea("Hacer las compras", prioridad="alta")
mostrar_tareas()"""

def buscar_tarea_por_id(id_buscado):
    for tarea in lista_tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None

"""tarea_encontrada = buscar_tarea_por_id(1)
if tarea_encontrada:
    print(f"\nBusqueda exitosa: {tarea_encontrada["descripcion"]}")
else:
    print("\nBusqueda fallida Tarea no encontrada")

tarea_fantasma = buscar_tarea_por_id(99)
if not tarea_fantasma:
    print("Búsqueda de tarea inexistente funcionó correctamente.")"""

def marcar_tarea_completada (id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        tarea["completada"] = True
        print(f"✅ Tarea '{tarea['descripcion']}' marcada como completada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")

def eliminar_tarea(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        lista_tareas.remove(tarea)
        print(f"✅ Tarea '{tarea['descripcion']}' eliminada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")

# ... (definiciones de funciones y pruebas aquí arriba) ...
# ¡Puedes comentar o eliminar las pruebas para tener un programa limpio!
while True:
    print("\n===== MENÚ TO-DO LIST =====")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        desc = input("Descripción de la nueva tarea: ")
        prio = input("Prioridad (alta, media, baja): ")
        agregar_tarea(desc, prio)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        id_t = int(input("ID de la tarea a completar: "))
        marcar_tarea_completada(id_t)
    elif opcion == '4':
        id_t = int(input("ID de la tarea a eliminar: "))
        eliminar_tarea(id_t)
    elif opcion == '0':
        print("¡Hasta pronto!")
        break # Rompe el bucle while
    else:
        print("❌ Opción no válida. Inténtalo de nuevo.")