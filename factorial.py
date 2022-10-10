#Realizar un programa que calcule el factorial de un número

import time

def factorial(n):
    resultado = 1
    index = 0

    while(index < n):
        index = index+1
        resultado = resultado*index
    return resultado

    
def factorial_for(n):
    resultado=1
    
    for i in range(1,n+1):
        resultado=resultado*i
    return resultado


#RECURSIVIDAD
def factorial_rec(n):
    if(n==1):
        return 1
    if(n==0):
        return 1
    else:
        return n*factorial_rec(n-1)
    
n=int(input("Dime un numero: "))
print("El factorial de", n, "es ",factorial_rec(n))


print("FACTORIAL WHILE")
inicio=time.time()
factorial(n)
fin=time.time()
total=fin-inicio

print("El programa ha tardado ", total, " segundos")

print("FACTORIAL FOR")
inicio=time.time()
factorial_for(n)
fin=time.time()
total=fin-inicio

print("El programa ha tardado ", total, " segundos")

print("FACTORIAL RECURSIVO")
inicio=time.time()
factorial_rec(n)
fin=time.time()
total=fin-inicio
print("El programa ha tardado ", total, " segundos")