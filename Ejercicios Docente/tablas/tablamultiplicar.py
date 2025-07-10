num_tabla = int(input( "introduce el numero de la tabla: " ))
print(f"--- Tabla del {num_tabla} ---")
for i in range(1, 11):
  resultado = num_tabla * i
  print(f"{num_tabla} x {i} = {resultado}")

print ("--- Fin del programa tablaMultiplicar --- Jim Requena")