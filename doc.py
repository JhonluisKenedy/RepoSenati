

def calculadora():
    print("*********************************************************")
    print("***************Bienvenido a la calculadora***************")
    print("*********************************************************")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print("-----------------------------------------------------------")
    
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Indefinido (No se puede dividir entre cero)"

    print(f"La suma   es: {suma}")
    print(f"La resta  es: {resta}")
    print(f"La multiplicación es: {multiplicacion}")
    print(f"La división  es: {division}")

calculadora()
