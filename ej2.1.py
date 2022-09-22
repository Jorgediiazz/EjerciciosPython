#Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, liquido, vapor) en función de su temperatura
temp = 0.0

#Pedir temperatura
temp = float(input("Dime la temperatura: "))

#Condicional
if (temp < 0):
     print(temp, "Su estado es hielo")
else:
    if (temp >= 100):
        print(temp, "Su estado es vapor")
    else:
        print(temp, "su estado es liquido")