operador = ""
operacion = None

numero = input("Digite el primer número: ").strip()
while not (numero.isdigit() or numero.startswith("-") and numero[1:].isdigit()):
    numero = input("Número inválido. Digite nuevamente: ").strip()
if numero.isdigit():
    operacion = float(numero)
elif numero.startswith("-"):
    operacion = float(numero[1:])*-1

while operador != "=":
    operador = input("Operador (+, -, *, /, //, %, **, =): ")
    if operador == "=":
        print("Resultado:", operación)
    else:
        numero = input("Digite otro número: ").strip()
        while not (numero.isdigit() or (numero.startswith("-") and numero[1:].isdigit())):
            numero = input("Número inválido. Digite nuevamente: ").strip()
        if numero.isdigit():
            numero = int(numero)
        elif numero.startswith("-"):
            numero = int(numero[1:])*-1
        if operador == "+":
            operacion += numero
        elif operador == "-":
            operacion -= numero
        elif operador == "*":
            operacion *= numero
        elif operador == "/":
            if numero != 0:
                operacion /= numero
            else:
                print("No se puede dividir entre 0")
        elif operador == "//":
            if numero != 0:
                operacion //= numero
