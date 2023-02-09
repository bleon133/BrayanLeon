#Misión 3 - Brayan Steven León Martinez - G5-6:00 AM A 10:00AM
opcion = -1
nTalentos,suma = 0,0
flag1,flag2,flag3,flag4,flag5,flag6 = False, False, False, False, False, False
talentos = [],[],[],[],[],[]
while opcion != 13:
    opcion = input('''Menú - Misión 3
1. Número de talento a registrar
2. Registro de Código y Nombre de cada talento
3. Registro de la nota de la Misión 1 de cada talento
4. Registro de la nota de la Misión 2 de cada talento
5. Registro de la nota de la Misión 3 de cada talento
6. Registro de la nota de la Prueba de Nivel de cada talento
7. Talento con la mejor nota de la Misión 1
8. Talento con la mejor nota de la Misión 2
9. Talento con la mejor nota de la Misión 3
10. Talentos con sus respectivos promedios
11. Código, Nombre y Notas de cada talento
12. Nombre del talento que desarrollo el programa
13. Salir
Elegir una opción: ''')
    match opcion:
        case '1':
            if flag1 == False:
                print("")
                nTalentos = int(input("Ingresar el número de talentos que desea registrar: "))
                while nTalentos < 1:
                    print("")
                    print("Error: Debe registrar cantidad valida.")
                    nTalentos = int(input("Ingresar el número de talentos que desea registrar: "))
                    print("")
                flag1 = True
                print("")
            else:
                print("")
                print("Error: Ya definio la cantidad de talentos a registrar. No puede repetir esta opción.")
                print("")
        case '2':
            if flag1 == True:
                print("")
                for i in range(nTalentos):
                    talentos[0].append(input(f"Ingresar el código del talento #{i+1}: "))
                    while talentos[0].count(talentos[0][i]) > 1:
                        print("Error: Código existente, por favor digitar uno valido y diferente.")
                        talentos[0][i] = input(f"Ingresar el código del talento #{i+1}: ")
                    talentos[1].append(input(f"Ingresar el nombre del talento #{i+1}: "))
                    while talentos[1][i] == "":
                        print("Error: Debe ingresar un nombre valido, no debe quedar vacío.")
                        talentos[1][i] = input(f"Ingresar el nombre del talento #{i+1}: ")
                flag2 = True
                print("")
            else:
                print("")
                print("Error: Debe primero realizar la opción 1.")
                print("")
        case '3':
            if flag1 == True and flag2 == True:   
                print("")
                for i in range(len(talentos[1])):
                    talentos[2].append(float(input(f"Ingresar la nota de la misión 1 del talento {talentos[1][i]}:")))
                    while talentos[2][i] < 0 or talentos[2][i] > 100:
                        print("Error: La nota digitada no esta dentro del rango, debe estar entre 0 a 100")
                        talentos[2][i] = (float(input(f"Ingresar la nota de la misión 1 del talento {talentos[1][i]}:")))
                flag3 = True
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '4':
            if flag1 == True and flag2 == True and flag3 == True:   
                print("")
                for i in range(len(talentos[1])):
                    talentos[3].append(float(input(f"Ingresar la nota de la misión 2 del talento {talentos[1][i]}:")))
                    while talentos[3][i] < 0 or talentos[3][i] > 100:
                        print("Error: La nota digitada no esta dentro del rango, debe estar entre 0 a 100")
                        talentos[3][i] = (float(input(f"Ingresar la nota de la misión 1 del talento {talentos[1][i]}:")))
                flag4 = True
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '5':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True:   
                print("")
                for i in range(len(talentos[1])):
                    talentos[4].append(float(input(f"Ingresar la nota de la misión 3 del talento {talentos[1][i]}:")))
                    while talentos[4][i] < 0 or talentos[4][i] > 100:
                        print("Error: La nota digitada no esta dentro del rango, debe estar entre 0 a 100")
                        talentos[4][i] = (float(input(f"Ingresar la nota de la misión 1 del talento {talentos[1][i]}:")))
                flag5 = True
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '6':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                for i in range(len(talentos[1])):
                    talentos[5].append(float(input(f"Ingresar la nota de la prueba de nivel del talento {talentos[1][i]}:")))
                    while talentos[5][i] < 0 or talentos[5][i] > 100:
                        print("Error: La nota digitada no esta dentro del rango, debe estar entre 0 a 100")
                        talentos[5][i] = (float(input(f"Ingresar la nota de la prueba de nivel del talento {talentos[1][i]}:")))
                flag6 = True
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '7':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                print("Nombre  Misión1")
                for i in range(len(talentos[2])):
                    if talentos[2][i] == max(talentos[2]): 
                        print(talentos[1][i], end='\t')
                        print(talentos[2][i], end='\t')
                        print("")
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '8':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                print("Nombre  Misión2")
                for i in range(len(talentos[3])):
                    if talentos[3][i] == max(talentos[3]): 
                        print(talentos[1][i], end='\t')
                        print(talentos[3][i], end='\t')
                        print("")
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '9':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                print("Nombre  Misión3")
                for i in range(len(talentos[4])):
                    if talentos[4][i] == max(talentos[4]): 
                        print(talentos[1][i], end='\t')
                        print(talentos[4][i], end='\t')
                        print("")
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '10':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                print("Nombre  Promedio")
                for i in range (len(talentos[1])):
                    print(talentos[1][i], end='\t')
                    for j in range (2,6):
                        suma += talentos[j][i]
                    print(suma/4, end='\t')
                    print("")
                    suma = 0
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '11':
            if flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True:   
                print("")
                print("Código  Nombre  Misión1  Misión2  Misión3  P.Nivel")
                for i in range (len(talentos[1])):
                    for j in range (6):
                        print(talentos[j][i], end='\t')
                    print("")
                print("")
            else:
                print("")
                print("Error: Debe primero realizar las anteriores opciones.")
                print("")
        case '12':
            print("")
            print("Creador: Brayan Steven León Martinez")
            print("")
        case '13':
            print("")
            print("Fin del Programa. Gracias")
            break
        case default:
            print("")
            print("Error: Opción Invalida")
            print("")