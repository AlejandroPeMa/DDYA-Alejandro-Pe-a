def positivo(n):
    if n > 0:
        print(n, "es positivo.")
        return 1
    elif n < 0:
        print(n, "es negativo.")
        return -1
    else:
        print(n, "es cero.")
        return 0


def fibonacci(n):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    if n in fib:
        print(n, "pertenece a Fibonacci.")
    else:
        print(n, "no pertenece a Fibonacci.")


def primo(n):
    if n < 2:
        print(n, "no es primo.")
        return

    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    if divisores == 2:
        print(n, "es primo.")
    else:
        print(n, "no es primo.")


def analizar_numero(n):
    estado = positivo(n)
    fibonacci(n)
    primo(n)
    return estado


def sumar_intermedios(a, b):
    if a < b:
        menor, mayor = a, b
    else:
        menor, mayor = b, a

    suma = 0
    for i in range(menor, mayor + 1):
        suma += i

    return suma


def multiplicar_intermedios(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    mult = 1
    for i in range(menor, mayor + 1):
        mult *= i
    return mult

def main():
    entrada = input("Ingrese 2 números enteros separados por una coma: ")
    a, b = entrada.split(",")
    a = int(a)
    b = int(b)

    estado_a = analizar_numero(a)
    estado_b = analizar_numero(b)

    if estado_a == -1 and estado_b == -1:
        resultado = multiplicar_intermedios(a, b)
        print("Los dos números son negativos, se multiplican los intermedios:", resultado)
    else:
        resultado = sumar_intermedios(a, b)
        print("Se suman los intermedios:", resultado)

    if resultado % 2 == 0:
        print("El resultado es par, se eleva al cubo:", resultado ** 3)
    else:
        print("El resultado es impar, se eleva al cuadrado:", resultado ** 2)


main()

# Punto 7: aca lo que hago es lo mismo de arriba pero con el codigo
# estudiantil. Como el codigo es un monton de numeros pegados, los voy
# cogiendo de a 2 en 2 y les hago todo el proceso de siempre (ver si es
# positivo, si es fibonacci, si es primo y despues sumar o multiplicar).

# Punto 8: aca solo pido el dia, el mes y el año por separado, y como ya
# tengo el codigo estudiantil de antes, los junto todos en un solo texto
# para armar la fecha completa.

# Punto 9: aca recorro la fecha letra por letra. Si encuentro un numero
# o el "/" lo salto, y si es letra miro si es vocal o consonante y lo
# voy diciendo.

# Punto 10: es lo mismo que el punto de arriba pero en vez de solo decir
# vocal o consonante, le voy sumando 1 a un contador cada vez, para al
# final saber cuantas vocales y consonantes hay en total.

