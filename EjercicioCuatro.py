import math

print("Ingresa el número de puntos (enteros positivos), para salir presione 0")
num = 1
nums = []

while(num > 0):
    num = int(input())
    if(num > 0):
        nums.append(num)

if(len(nums) > 0):
    for j in range(0,len(nums)):
        resultado = (((math.pow(nums[j],4)) - (6*math.pow(nums[j],3)) + (23*math.pow(nums[j],2)) - (18*nums[j])) / 24) + 1
        print("Las regiones del círculo son: ",resultado)
