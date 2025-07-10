"""las tres comillas son para documentar la funcion o Docstring"""
from funcione2 import look_area_rectangulo

#print("\nCalcualdora simple")
#num1 = int(input("\nIngrese un numero: "))
#num2 = int(input("\nIngrese otro numero: "))

#print(suma_fun(num1,num2))
 
def main():
    base = int(input("Ingrese la base: "))
    altura = int (input("Ingrese la altura: "))
    look_area_rectangulo(2, base, altura)

if __name__ == "__main__":
    main()