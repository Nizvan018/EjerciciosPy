print("Ingresa los números (A, B): ")
cdn = input()

espacio = cdn.find(" ")
numUnoPosicion = espacio
numDosPosicion = espacio

numUno = int(cdn[:numUnoPosicion])
numDos = int(cdn[numDosPosicion:])

print(numUno + numDos)
