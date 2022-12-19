"""
Tarea # 3
"""
import math

p = input("Ingrese su peso en kg, por favor: ")

p = int(p)

a = input("Ingrese su altura en metros, por favor: ")

a = int(a)

a /= 100

a *= a 

a = round(a, 3)

print(a)

imc = p / a

imc = round(imc,2)

print("Su IMC es {}".format(imc))
