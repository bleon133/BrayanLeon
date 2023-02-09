print("Nombre: Brayan Steven León Martinez")
print("TALLER 2 - EJERCICIOS DE ALGORITMIA ESTRUCTURA CONDICIONAL")
exercise= input('''1. Ejercicio 1
2. Ejercicio 2
3. Ejercicio 3
4. Ejercicio 4
5. Ejercicio 5
6. Ejercicio 6
7. Ejercicio 7
8. Ejercicio 8
9. Ejercicio 9
Elegir el ejercicio a visualizar: ''')
match exercise:
    case '1':
        print("Leer dos (2) números y los imprima en forma ascendente.")
        num1 = float(input("Digitar el primer número: "))
        num2 = float(input("Digitar el segundo número: "))
        if(num2 > num1):
            print(f"Forma Ascendente: {num1} y {num2}")
        else:
            print(f"Forma Ascendente: {num2} y {num1}")
    case '2':
        print('''(Sentencia match) Diseñar un algoritmo que lea por teclado un número comprendido entre 1 y 10. Se desea visualizarsi el número es par o impar. En primer lugar, se deberá detectar si 
el número está comprendido en el rango válido (1 a 10) y a continuación si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”;si es 2, 4, 6, 8, 10, escribir un mensaje de “par”.''')
        oddOrEvenNum= input("Digitar un número entero entre 1 al 10: ")
        match oddOrEvenNum:
            case '1'|'3'|'5'|'7'|'9':
                print(f"El número {oddOrEvenNum} es impar.")
            case '2'|'4'|'6'|'8'|'10':
                print(f"El número {oddOrEvenNum} es par.")
            case default: 
                print("Error: Valor Incorrecto.")
    case '3':
        print('''(Sentencia match) Diseñar un algoritmo que lea un número entero entre 1 y 10, y nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído no está comprendido 
entre 1 y 10 mostrar un mensaje de error.''')
        letterNum= input("Digitar un número entero entre 1 al 10: ")
        match letterNum:
            case '1':
                print("Uno")
            case '2':
                print("Dos")
            case '3':
                print("Tres")
            case '4':
                print("Cuatro")
            case '5':
                print("Cinco")
            case '6':
                print("Seis")
            case '7':
                print("Siete")
            case '8':
                print("Ocho")
            case '9':
                print("Nueve")
            case '10':
                print("Diez")
            case default:
                print("Error: Valor Incorrecto.")
    case '4':
        print('''Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta lo siguiente:
• toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
• cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 100 pesos.''')
        duration= int(input("Digitar en número entero la duración en minutos la llamada realizada: "))
        if(duration <= 3 and duration > 0):
            print(f'Tras haber durado {duration} minutos en la llamada, el total a pagar es de: 200 pesos.')
        elif(duration > 3):
            print(f'Tras haber durado {duration} minutos en la llamada, el total a pagar es de: {200+((duration-3)*100)} pesos.')
        else:
            print("Error: Valor Incorrecto.")
    case '5':
        print('''En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros y Y conejos blancos. Hacer un algoritmo que:
• Imprima la cantidad de conejos vendida
• Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de los conejos negros, imprima el monto total de la venta.
• Imprima el color de los conejos que se vendieron más.''')
        priceWhite= float(input("Digitar el precio de un conejo blanco: "))
        priceBlack= float(input("Digitar el precio de un conejo negro: "))
        whiteRabbits= int(input("Digita el número de conejos blancos a comprar: "))
        blackRabbits= int(input("Digita el número de conejos negros a comprar: "))
        if(priceWhite > 0 and priceBlack > 0 and whiteRabbits > 0 and blackRabbits > 0):
            if(whiteRabbits > blackRabbits):
                print('''Factura: 
• El conejo mayormente vendido es el de color Blanco.''')
            elif(whiteRabbits == blackRabbits):
                print('''Factura: 
• Los dos colores de conejos fueron por igual cantidad vendidos.''')
            else:
                print('''Factura: 
• El conejo mayormente vendido es el de color Negro.''')
            print(f'''• Total de conejos vendidos: {whiteRabbits+blackRabbits}.
• Precio Total de conejos blancos: {priceWhite*float(whiteRabbits)}.
• Precio Total de conejos negros: {priceBlack*float(blackRabbits)}.
• Precio Total de conejos vendidos: {(priceWhite*float(whiteRabbits))+(priceBlack*float(blackRabbits))}.''')
        else:
            print("Alguno de los valores digitados son invalidos.")
    case '6':
        print('''Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes, determinadas sobre las siguientes condiciones:
• NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante tendrá 3 evaluaciones.
• NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante presentara 2 trabajos.
• NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
• Nota mínima 1,0 nota máxima: 5,0''')
        exam1= float(input("Digitar la nota del examen 1: "))
        exam2= float(input("Digitar la nota del examen 2: "))
        exam3= float(input("Digitar la nota del examen 3: "))
        work1= float(input("Digitar la nota del trabajo 1: "))
        work2= float(input("Digitar la nota del trabajo 2: "))
        if((exam1 >= 1.0 and exam1 <= 5.0) and (exam2 >= 1.0 and exam2 <= 5.0) and (exam3 >= 1.0 and exam3 <= 5.0) and (work1 >= 1.0 and work1 <= 5.0) and (work2 >= 1.0 and work2 <= 5.0)):
            print(f'''Resultados:
• NOTA PREVIOS: {((exam1+exam2+exam3)/3)*60/100}
• NOTA TRABAJOS: {((work1+work2)/2)*40/100}
• NOTA FINAL: {(((exam1+exam2+exam3)/3)*60/100) + (((work1+work2)/2)*40/100)}''')
        else:
            print("Error: Las notas deben de estar entre 1.0 a 5.0.")
    case '7':
        print('''Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original, cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 1 el descuento 
es del 10% y si la clave es 2 el descuento es del 20% (solo existen dos claves).''')
        discount= 0.0
        key= int(input("Digitar la clave para el descuento(1: 10% o 2: 20%): "))
        if(key == 1 or key == 2):
            articleName= str(input("Digitar el nombre del artículo: "))
            originalPrice= float(input(f"Digitar el precio original de {articleName}: "))
            amount= int(input(f"Digitar la cantidad a comprar de {articleName}: "))
            if(key == 1):
                discount= 1.0
                print(f'''Factura: 
• Clave: {key}, descuendo del 10%.''')
            elif(key == 2):
                discount= 2.0
                print(f'''Factura:
• Clave: {key}, descuendo del 20%.''')
            print(f'''• Nombre del Artículo: {articleName}.
• Precio Original (respecto a la cantidad): {originalPrice*amount}.
• Cantidad: {amount}.
• Precio con Descuento: {(originalPrice*amount)-((originalPrice*amount)*discount/100)}''')
        else:
            print("Error: Clave digitada incorrecta.")
    case '8':
        print('''En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología. El presupuesto anual del hospital se reparte a estas tres 
(3) áreas; usted debe realizar un algoritmo que permita ingresar el valor del presupuesto anual, ingresar el porcentaje correspondiente a cada área, 
realizar el cálculo del presupuesto que corresponde a cada área,si la suma de los porcentajes no corresponde al 100% debe mostrar un mensaje de error.
Mostrar el porcentaje asignado a cada área y el presupuesto obtenido.''')
        preAnual = float(input("Digitar el presupuesto Anual: "))
        porPsiq = float(input("Digitar el porcentaje de Psiquiatría: "))
        porPedi = float(input("Digitar el porcentaje de Pediatría: "))
        porTrau = float(input("Digitar el porcentaje de Traumatología: "))
        if((porPsiq + porPedi + porTrau) == 100):
            print(f'''Resultados:
• Psiquiatría: El porcentaje asignado es {porPsiq}%, por ende, el presupuesto del área es {preAnual*porPsiq/100}.
• Pediatría: El porcentaje asignado es {porPedi}%, por ende, el presupuesto del área es {preAnual*porPedi/100}.
• Traumatología: El porcentaje asignado es {porTrau}%, por ende, el presupuesto del área es {preAnual*porTrau/100}.''')
        else:
            print("Error: Los porcentajes deben sumar 100%")
    case '9':
        print('''Diseñar un algoritmo para determinar el precio del tiquete de ida y vuelta en avión, conociendo la distancia a recorrer, sabiendo 
que si el número de días de estancia es superior o igual a 7 y la distancia superior a 800 km el billete tiene una reducción del 30%. El precio por 
km es de $2,5 dólares.''')
        distance= float(input("Digitar la distancia a recorrer (km): "))
        days= int(input("Digitar los días de estancia: "))
        if(days >= 7 and distance > 800):
            ticketPrice= (2.5*distance)-((2.5*distance)*30/100)
        else:
            ticketPrice= (2.5*distance)
        print(f"Resultado: El precio a pagar es de: {ticketPrice}")
    case default:
        print("Error: Opción Incorrecta.")
    
