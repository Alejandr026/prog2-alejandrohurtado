def cal_area_rectangulo(base, altura):
    return base * altura
"""Calcula el area de un rectangulo"""
def look_area_rectangulo(num, base, altura):
    area = cal_area_rectangulo(base, altura)
    print(f"El area del rectangulo {num} ({base} x {altura}) es: {area}")

def main():
    look_area_rectangulo(1, 10, 20)
    look_area_rectangulo(2, 7, 3)
    look_area_rectangulo(3, 8, 2)

    print("___Alejandro Hurtado____")

if __name__ == "__main__":
    main()