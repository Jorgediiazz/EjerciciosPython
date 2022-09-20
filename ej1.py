#Introducir la hora del dia en horas, minutos y segundos.
#Calcular cuantós segundos han transcurrido desde el contenido del día.

hora = 0
minu = 0
seg = 0
#Imprimir
hora= int(input("Introduce la hora:"))
minu= int(input("Introduce los minutos:"))
seg= int(input("Introduce los segundos:"))
hora=int(hora)*3600
minu=int(minu)*60
seg= int(hora)+int(minu)+int(seg)
print("El resultado es", seg)