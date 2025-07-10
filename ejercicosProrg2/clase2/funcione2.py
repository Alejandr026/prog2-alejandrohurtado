def suma_fun(num1, num2):

    resulado = int(num1 + num2)
    return ("La suma de " + str(num1) + " + " + str(num2) + " es: " + str(resulado))
"""Funcion simple de suma Final"""

#Funciones de refactorisacion

def cal_area_rectangulo(base, altura):
    return base * altura
"""Calcula el area de un rectangulo"""
def look_area_rectangulo(num, base, altura):
    area = cal_area_rectangulo(base, altura)
    print(f"El area del rectangulo {num} ({base} x {altura}) es: {area}")