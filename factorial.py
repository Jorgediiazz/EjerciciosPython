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
    
