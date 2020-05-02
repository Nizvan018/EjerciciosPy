print("Introduce un número: ")
num = int(input())
resultado = 0

if num <= 10000 and num > 0:
    for i in range(1, num + 1):
        resultado = resultado + i
    print("El resultado es: ",resultado)
elif num < 0:
    for i in range(num, -1):
        resultado = resultado + i
    print("El resultado es: ", resultado)
else:
    print("El número es inválido")
