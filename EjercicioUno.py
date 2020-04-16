print("Ingresa los números (A, B): ")
cdn = input()

espacio = cdn.find(" ")
numUnoPosicion = espacio
numDosPosicion = espacio

numUno = int(cdn[:numUnoPosicion])
numDos = int(cdn[numDosPosicion:])

if numUno >= 0 and numDos <= 10:
    print(numUno + numDos)
else:
    print("Los núeros son inválidos: A >= 0, B <= 10")
