#Realizar un programa que calcule el factorial de un número

def factorial(n):
    resultado = 1
    index = 0
    
    while(index < n):
        index = index+1
        resultado = resultado*index
    return resultado
n=int(input("Dime un numero: "))
print("El factorial de ", n, "es ", factorial(n))

def factorial_for(n):
    resultado=1
    
    for i in range(1,n+1):
        resultado=resultado*i
    return resultado
n=int(input("Dime un numero: "))
print("El factorial de ", n, "es ", factorial_for(n))