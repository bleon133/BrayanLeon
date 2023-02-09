#Profesor de matemáticas -> Alumno: Código,Nombre y Promedio
#Por medio del promedio, revisar cuantos: 
#Aprobaron (mayor o igual a 7)
#Habilitan en Diciembre: menor a 7 y mayor o igual a 4
#Habilitan examen en marzo: menor a 4
#Imprimir el código y nombre de los mejores alumnos con mejor promedio
#Hacer lo anterior con un menú
""" alumnos = []
alumno = {}
first,second,third,actual,anterior = 0,0,0,0,0
nStudents,aproved,decEnable,marEnable = 0,0,0,0
flag1,flag2 = False,False
option = -1
while option != 5:
    option = input('''CLASE MATEMÁTICAS
1. Digitar la cantidad de alumnos
2. Digitar datos del alumno y promedio
3. Visualizar cuantos aprobarón, habilitan en diciembre y habilitan examen en marzo
4. Visualizar los 3 alumnos con mejor promedio
5. Salir
Digitar opción: ''')
    match option:
        case '1':
            nStudents = int(input("Digitar cantidad de alumnos: "))
            flag1 = True
        case '2':
            if flag1 == True:
                for i in range(nStudents):
                    alumno["Codigo"] = input(f"Digitar el código del alumno #{i+1}: ")
                    alumno["Nombre"] = input(f"Digitar el nombre del alumno #{i+1}: ")
                    alumno["Promedio"] = input(f'Digitar el promedio de {alumno["Nombre"]}: ')
                    while float(alumno["Promedio"]) < 0 or float(alumno["Promedio"]) > 10:
                        print("Error: El valor debe estar entre 0 a 10.")
                        alumno["Promedio"] = input(f'Digitar el promedio de {alumno["Nombre"]}: ')
                    alumnos.append(alumno)
                    alumno = {}
                flag2 = True
            else:
                print("Error: Debe realizar primero la opción 1.")
        case '3':
            if flag1 == True and flag2 == True:
                for i in range(len(alumnos)):
                    if float(alumnos[i]["Promedio"]) >= 7:
                        aproved += 1
                    elif float(alumnos[i]["Promedio"]) < 7 or float(alumnos[i]["Promedio"]) >= 4:
                        decEnable += 1
                    else : 
                        marEnable += 1
                print(f"Aprobarón: {aproved}. Habilitan en Diciembre: {decEnable}. Habilitan Examen en Marzo: {marEnable}.")
            else:
                print("Error: Debe realizar la opcion 1 y 2.")
        case '4':
            if flag1 == True and flag2 == True:
                for i in range(len(alumnos)):
                    if (i == 0):
                        first =  i
                    else:
                        actual =  i
                    if(len(alumnos) == 2):
                        if(float(alumnos[first]["Promedio"]) < float(alumnos[actual]["Promedio"])):
                            first = actual
                    elif(len(alumnos) == 3): # 2 Mejores Alumnos
                        if(i == 1):
                            if (float(alumnos[first]["Promedio"]) < float(alumnos[actual]["Promedio"])):
                                second = first
                                first = actual
                            else:
                                second = actual
                        else:
                            if (float(alumnos[actual]["Promedio"]) > float(alumnos[first]["Promedio"])):
                                first = actual
                                second = first
                            elif (float(alumnos[actual]["Promedio"]) < float(alumnos[first]["Promedio"]) and float(alumnos[actual]["Promedio"]) > float(alumnos[second]["Promedio"])):
                                second = actual
                    elif(len(alumnos) > 3): # 3 Mejores Alumnos
                        if(i == 1):
                            if (float(alumnos[first]["Promedio"]) < float(alumnos[actual]["Promedio"])):
                                second = first
                                first = actual
                            else:
                                second = actual
                        elif(i == 2):
                            if (float(alumnos[actual]["Promedio"]) > float(alumnos[first]["Promedio"])):
                                second = first
                                first = actual
                            else:
                                second = actual
                        elif(i >= 3):
                            if (float(alumnos[actual]["Promedio"]) > float(alumnos[first]["Promedio"])):
                                third = second
                                second = first
                                first = actual
                            elif (float(alumnos[actual]["Promedio"]) < float(alumnos[first]["Promedio"]) and float(alumnos[actual]["Promedio"]) > float(alumnos[second]["Promedio"])):
                                third = second
                                second = actual
                            elif (float(alumnos[actual]["Promedio"]) > float(alumnos[third]["Promedio"]) and float(alumnos[actual]["Promedio"]) < float(alumnos[first]["Promedio"]) and float(alumnos[actual]["Promedio"]) < float(alumnos[second]["Promedio"])):
                                third = actual
                    else:
                        print(f'Solo se lleno 1 alumno, es decir, {alumnos[i]["Nombre"]} con código {alumnos[i]["Codigo"]} sería el mejor')
                if(len(alumnos) == 2):
                    print(f'El mejor de los {len(alumnos)} es: 1.{alumnos[first]["Nombre"]}-{alumnos[first]["Codigo"]}')
                elif(len(alumnos) == 3):
                    print(f'Mejores de los {len(alumnos)} son: 1.{alumnos[first]["Nombre"]}-{alumnos[first]["Codigo"]} y 2.{alumnos[second]["Nombre"]}-{alumnos[second]["Codigo"]}')
                elif(len(alumnos) > 3):
                    print(f'Mejores de los {len(alumnos)} son: 1.{alumnos[first]["Nombre"]}-{alumnos[first]["Codigo"]}, 2.{alumnos[second]["Nombre"]}-{alumnos[second]["Codigo"]} y 3.{alumnos[third]["Nombre"]}-{alumnos[third]["Codigo"]}')
            else:
                print("Error: Debe realizar la opcion 1 y 2.")
        case '5':
            break
        case default:
            print("Error: Opción Incorrecta")
            print("") """

#TURBOCOEX -> nEstudiantes -> Nombre, Código, Nivel (Beginner, junior, senior)
#Verificar que no tengan códigos duplicados en el registro
#Pedir 3 notas por alumno -> Imprimir Promedio-NombreEst-Aprobó o Reprobó-Promedio General Del grupo
#Aprobó > >= 3.5 - Validad notas de 0 a 5

option = -1
while option != 7:
    option = input('''CLASE MATEMÁTICAS
1. Definir cantidad de estudiantes
2. Registrar datos estudiantes
3. Mostrar listado de estudiantes
4. Registrar notas estudiantes
5. Imprimir notas estudiantes
6. Acerca del Autor
7. Salir
Digitar opción: ''')