import random
print('''Nombre: Brayan Steven León Martinez
Taller: EJERCICIO DE ESTRUCTURA CÍCLICA (BUCLES)''')
opcion = -1
while opcion != 0:
    opcion = input('''---Ejercicios---
1. Ejercicio 1
2. Ejercicio 2
3. Ejercicio 3
4. Ejercicio 4
5. Ejercicio 5
6. Ejercicio 6
7. Ejercicio 7
8. Ejercicio 8
9. Ejercicio 9
10. Ejercicio 10
0. Salir
"Digitar el ejercicio a visualizar: ''')
    match opcion:
        case '1':
            print("Sumar una cantidad N números MAYORES a 0 utilizando MIENTRAS.")
            n = -1
            m = 0
            while n != 0:
                n = int(input("Digitar un número: "))
                m+=n
                print(f"Suma: {m}")
        case '2':
            print("Imprimir números aleatorios en el rango de 0 a 10 mientras el número no sea igual a cero.")
            x = -1
            while x != 0:
                x = random.randint(0,10)
                if(x != 0):
                    print(x, end=', ')
            print("")
        case '3':
            print("Imprimir 20 números aleatorios en el rango de 1 a 1000.")
            for i in range(1,21):
                print(random.randint(1,1000), end=', ')
            print("")
        case '4':
            print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.")
            y = int(input("Digitar un número positivo: "))
            if(y > 0):
                for i in range(1,y+1,2):
                    print(i, end=", ")
                print("")
            else:
                print("Error: Debe digitar números positivos, no negativos.")
        case '5':
            print('''Una persona debe realizar un muestreo con 20 personas para determinar el promedio de peso de los niños, jóvenes, adultos 
viejos que existen en su zona habitacional. Se determinan las categorías con base en la sig., tabla:
CATEGORIA EDAD
Niños 0 - 12
Jóvenes 13 - 29
Adultos 30 - 59
Viejos 60 en adelante''')
            children,young,adults,old,wChildren,wYoung,wAdults,wOld = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
            for i in range (1,21):
                age = int(input(f"Digitar edad persona {i}: "))
                weight = float(input(f"Digitar peso persona {i}: "))
                while age < 0 or weight <= 0:
                    print("Error: Vuelva a digitar pero con valores coherentes")
                    age = int(input(f"Digitar edad persona {i}: "))
                    weight = float(input(f"Digitar peso persona {i}: "))
                if(age > 0 and age <= 12):
                    children+=1
                    wChildren+=weight
                elif(age >= 13 and age <= 29):
                    young+=1
                    wYoung+=weight
                elif(age >= 30 and age <= 59):
                    adults+=1
                    wAdults+=weight
                else:
                    old+=1
                    wOld+=weight
            if(children == 0):
                children = 1.0
            if(young == 0):
                young = 1.0
            if(adults == 0):
                adults = 1.0
            if (old == 0):
                old = 1.0
            print(f'''Resultados:
*Niños: {wChildren/children}
*Jovenes: {wYoung/young}
*Adultos: {wAdults/adults}
*Viejos: {wOld/old}''')
        case '6':
            print('''Diseñen un algoritmo que imprima la siguiente secuencia:
1.1.1 - 1.1.2 - 1.1.3 - 1.1.4
1.2.1 - 1.2.2 - 1.2.3 - 1.2.4
1.3.1 - 1.3.2 - 1.3.3 - 1.3.4
1.4.1 - 1.4.2 - 1.4.3 - 1.4.4
1.5.1 - 1.5.2 - 1.5.3 - 1.5.4''')
            y=0
            n=0
            print("Desarrollo:")
            for n in range (1,6):
                for y in range (1,5):
                    if(y<4):
                        print(f"1.{n}.{y}", end=" - ")
                    else:
                        print(f"1.{n}.{y}", end="")
                print("")
        case '7':
            print('''Un Zoólogo pretende determinar el porcentaje de animales que hay en las siguientes tres categorías de edades: de 0 a 1 año, de más de 1 año y menos de 3 y de 3 o más años. El
zoológico todavía no está seguro del animal que va a estudiar. Si se decide por elefantes solo tomara una muestra de 20 de ellos; si se decide por las jirafas, tomara 15 muestras, y si son 
chimpancés tomara 40.''')
            category1,category2,category3,age = 0,0,0,0
            animalType = input('''---Tipo de Muestras---
1. Elefantes (20)
2. Jirafas (15)
3. Chimpancés (40)
0. Salir
Elegir el tipo de población a trabajar: ''')
            match animalType:
                case '1':
                    for i in range (1,21):
                        age = int(input(f"Digitar la edad de la muestra de elefante # {i}: "))
                        while age < 0 and age > 80:
                            print("Error: Edad Invalidad, vuelva a digitar.")
                            age = int(input(f"Digitar la edad de la muestra de elefante # {i}: "))
                        if(age >= 0 and age <= 1):
                            category1+=1
                        elif(age > 1 and age < 3):
                            category2+=1
                        else:
                            category3+=1
                    print(f'''Resultados-Promedios-Elefantes:
*De 0 a 1 año: {category1*100/i}
*De más de 1 año: {category2*100/i}
*De 3 o más años: {category3*100/i}''')
                case '2':
                    for i in range (1,16):
                        age = int(input(f"Digitar la edad de la muestra de jirafas # {i}: "))
                        while age < 0 and age > 80:
                            print("Error: Edad Invalidad, vuelva a digitar.")
                            age = int(input(f"Digitar la edad de la muestra de jirafas # {i}: "))
                        if(age >= 0 and age <= 1):
                            category1+=1
                        elif(age > 1 and age < 3):
                            category2+=1
                        else:
                            category3+=1
                    print(f'''Resultados-Promedios-Jirafas:
*De 0 a 1 año: {category1*100/i}
*De más de 1 año: {category2*100/i}
*De 3 o más años: {category3*100/i}''')
                case '3':
                    for i in range (1,41):
                        age = int(input(f"Digitar la edad de la muestra de chimpancés # {i}: "))
                        while age < 0 and age > 80:
                            print("Error: Edad Invalidad, vuelva a digitar.")
                            age = int(input(f"Digitar la edad de la muestra de chimpancés # {i}: "))
                        if(age >= 0 and age <= 1):
                            category1+=1
                        elif(age > 1 and age < 3):
                            category2+=1
                        else:
                            category3+=1
                    print(f'''Resultados-Promedios-Chimpancés:
*De 0 a 1 año: {category1*100/i}
*De más de 1 año: {category2*100/i}
*De 3 o más años: {category3*100/i}''')
                case '0':
                    break
                case default:
                    print("Error: Opción Incorrecta.")
        case '8':
            print('''Una compañía de seguros tiene contratados a una cantidad N vendedores. Cada vendedor hace tres ventas a la semana. Su política de pagos es que un vendedor
recibe un sueldo base, y además un 10% extra por comisiones del total de sus ventas. El gerente de la compañía desea saber cuánto dinero recibirá cada vendedor en una semana
por concepto de comisiones por las ventas, y cuanto será el total tomando en cuenta su sueldo base y sus comisiones.''')
            nSeller = int(input("Digitar el número de vendedores existentes en la Compañia de Seguros: "))
            for i in range (1,nSeller+1):
                baseSalary = 0
                sallerSalary = 0
                baseSalary = float(input(f"Digitar el sueldo base del vendendor #{i}: "))
                while baseSalary < 0:
                    print("Error: Sueldo Base Invalido, vuelva a digitar.")
                    baseSalary = float(input(f"Digitar el sueldo base del vendendor #{i}: "))
                for j in range (1,4):
                    sale = float(input(f"Digitar el valor de la venta #{j} del vendedor #{i}: "))
                    while sale < 0:
                        print("Error: Valor de la Venta Invalido, vuelva a digitar.")
                        sale = float(input(f"Digitar el valor de la venta #{j} del vendedor #{i}: "))
                    sallerSalary+=sale
                print(f'''Sueldo Semanal del Vendedor # {i}:
*Sueldo solo por comisión: {sallerSalary*10/100}
*Sueldo total: {baseSalary+(sallerSalary*10/100)}''')
        case '9':
            print('''Una agencia de venta de autos paga a su personal de ventas un salario de $950.000, más una comisión de $170.000 por cada auto vendido, y también un 5% 
extra del valor total de las ventas. Diseñar un algoritmo para calcular el salario de un vendedor en un determinado mes, realizando la lectura por pantalla del no de
automóviles vendidos y el valor de cada auto para hallar el monto total de ventas.''')
            totalAmount = 0
            carsSold = int(input("Digitar el número de autos vendidos: "))
            while carsSold < 0:
                print("Error: Número Invalido, vuelva a digitarlo")
                carsSold = int(input("Digitar el número de autos vendidos: "))
            for i in range(1,carsSold+1):
                carValue = float(input(f"Digitar el valor del auto #{i}: "))
                while carValue < 0:
                    print("Error: Número Invalido, vuelva a digitarlo")
                    carValue = float(input(f"Digitar el valor del auto #{i}: "))
                totalAmount+=carValue
            print(f"El salario del vendedor en el mes fue de: {950000+(170000*carsSold)+(totalAmount*5/100)}")
        case '10':
            print('''Hallar el promedio de calificaciones de un estudiante, teniendo en cuenta el nombre estudiante y 5 notas; calculando la 
nota final de acuerdo a los siguientes porcentajes: Dos (2) notas valen el 40% y las otras tres (3) valen el 60%.''')
            nota40,nota60 = 0.0, 0.0
            name= input("Digitar nombre del alumno: ")
            for i in range (1,6):
                if(i<3):
                    nota = float(input(f"Digitar la nota {i} equivalente al 40%: "))
                    while nota < 0 and nota >= 5:
                        print("Error: Número Invalido, debe ser entre 0 a 5")
                        nota = float(input(f"Digitar la nota {i} equivalente al 40%: "))
                    nota40 += nota
                else:
                    nota = float(input(f"Digitar la nota {i} equivalente al 60%: "))
                    while nota < 0 and nota >= 5:
                        print("Error: Número Invalido, debe ser entre 0 a 5")
                        nota = float(input(f"Digitar la nota {i} equivalente al 60%: "))
                    nota60 += nota
            print(f"El estudiante {name} tiene una nota final de {((nota40/2)*40/100) + ((nota60/3)*60/100)}")
        case '0':
            break
        case default:
            print("Error: Opción Incorrecta")