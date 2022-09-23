'''Escriba un algoritmo que determine la categoría deportiva de un usuario en función de su edad'''
#6 a 7 años : "BENJAMIN"
#8 a 9 años : "ALEVÍN"
#10 a 11 años : "INFANTIL"
#12 años y mas : "CADETE"

#Variables
edad=0

#Pregunto la edad
print("Dime la edad del niño:")
edad = int(input())

#Ejecución del problema
if (edad < 6):
 print ( " El niño no tiene categoría deportiva")
elif (edad == 6 or edad == 7):
 print ( "La categoria del niño es benjamín")   
elif ( edad == 8 or edad == 9):
 print ( "La categoria del niño es alevín")
elif (edad == 10 or edad == 11):
 print ( "La categoria del niño es infantil")
elif ( edad >= 12):
 print ( "La categoria del niño es cadete")