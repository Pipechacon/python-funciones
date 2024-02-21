print("MENU")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DIVISION")

opcion = int(input("seleccionar la operacion....: "))

if opcion == 1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    print("operacion resta")
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 - num2
    print("el resultado de la resta es:", resultado)
elif opcion == 3:
    print("operacion multiplicacion")
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 * num2
    print("el resultado de la multiplicacion es:", resultado)

elif opcion == 4:
    print("operacion division")
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 / num2
    print("el resultado de la division es:", resultado)
else:
    print("Opción no válida")