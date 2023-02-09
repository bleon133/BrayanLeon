'''
print("Calcular el perimetro y el área de un rectángulo dada su base y su altura")
base= float(input("Digitar la base del rectángulo: "))
altura= float(input("Digitar la altura del rectángulo: "))
perimetro= 2*(base+altura)
area= base*altura
print(f'El perimetro del rectángulo es: {perimetro} y el área es: {area}') 
'''

'''
print("Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C=(F-32)*5/9")
fahrenheit= float(input("Digitar la valor en Fahrenheit que desea convertir: "))
celsius= (fahrenheit-32)*5/9
print(f'La conversión del valor {fahrenheit} en fahrenheit \n a celsius es: {round(celsius,2)}')
'''

'''
print("Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra")
compra= int(input("Digitar el total de la compra sin tener en cuenta el descuento: "))
descuento= compra-((compra*15)/100)
print(f'El total a pagar teniendo cuenta el descuento es: {descuento}')
'''

'''
print("Calculadora para sacar nota final. Tener en cuenta que las notas van de 0 a 5")
calificacion1= float(input("Digitar la nota de la primera calificación parcial: "))
calificacion2= float(input("Digitar la nota de la segunda calificación parcial: "))
calificacion3= float(input("Digitar la nota de la tercera calificación parcial: "))
examenFInal= float(input("Digitar nota del examen final: "))
trabajoFInal= float(input("Digitar la nota del trabajo final: "))
notaFInal= (((calificacion1+calificacion2+calificacion3)/3)*55/100) + (examenFInal*30/100) + (trabajoFInal*15/100)
print(f'La nota final es: {notaFInal}')
'''

'''
print("Una persona recibe un préstamo de U$10,000.00 de un banco y desea saber cuánto pagará de interés, en un mes si el banco le cobra una tasa del 27% anual")
intereses=(10000*27/100)/12
print("Debe pagar en intereses mensualmente es: ", intereses)
'''

'''
print("Calcular el porcentaje de niños y niñas en una aula")
hombres= int(input("¿Cuantos hombres hay en el Aula?"))
mujeres= int(input("¿Cuantas mujeres hay en el Aula?"))
ph=(hombres*100)/(hombres+mujeres)
pm=(mujeres*100)/(hombres+mujeres)
print(f'En el aula hay {ph}% hombres y {pm}% mujeres')
'''

'''
print("Calcular el monto a pagar en una cabina de internet si el costo por hora es de 1500 y por cada 5 horas te dan una hora de promoción gratis, sabiendo que la permanencia en la cabina fueron de 12 horas.")
horas= int(input("¿Cuantas horas permanecio en la cabina?"))
precio= (1500*(horas-(horas//5)))
print("Debe pagar: ", precio)
'''