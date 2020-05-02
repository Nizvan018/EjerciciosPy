print("Introduce los números")
x = False
y = False
i = 2
j = 0
lista = []
listaF = [1]

while x == False and y == False:
    n = int(input())
    if n >= 1 and n <= 1500:
        lista.append(n)
    elif n == 0:
        x = True
    else:
        print("Número inválido")
        y = True

if y == False and lista:
    while len(listaF) < max(lista):
        d = 2
        feo = False
        cont = 0

        while d <= i:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                feo = True

            if d != 2 and d != 3 and d != 5:
                p = 1
                contPrim = 0
                while p <= d:
                    if d % p == 0:
                        contPrim = contPrim + 1
                    p = p +1
                if contPrim <= 2:
                    if i % d == 0:
                        feo = False

            if feo == False:
                cont = cont + 1

            d = d + 1

        if feo == True and cont == 0:
            listaF.append(i)

        i = i + 1

print()
for j in range(0,len(lista)):
    print("[",listaF[lista[j] - 1],"]",end = "")
