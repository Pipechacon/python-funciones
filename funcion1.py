def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

def resta():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)

def multiplicacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)

def division():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("No se puede dividir entre cero.")

print("MENU")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DIVISION")

opcion = int(input("Seleccionar la operación....: "))

if opcion == 1:
    suma()
elif opcion == 2:
    resta()
elif opcion == 3:
    multiplicacion()
elif opcion == 4:
    division()
else:
    print("Opción no válida")
