""" import random
lista=[]
suma=0
for i in range(10):
    lista.append(random.randint(1,10))
for j in range(10):
    suma+=lista[j]
print(lista)
print(suma) """

""" lista=[10,0,3,61,9,20,17,8,2,1]
menor = lista[0]
for i in range(10):
    if(lista[i] < menor):
        menor=lista[i]
print(menor) """

""" lista=[10,0,3,61,9,20,17,8,2,1]
lista.sort()
print(lista[len(lista)-1]) """

""" lista=[10,0,3,61,9,20,17,8,2,1]
respuesta=lista.index(61)
print(respuesta) """

""" lista=[10,0,3,61,9,20,17,8,2,1]
# print(lista.pop())
lista.pop()
lista.pop(2)
print(lista) """

paso1,paso2 = False,False
opcion,notaInd = 0,0.0
nombresNotas = [],[]
while opcion != 5:
    opcion = input('''1. Ingresar 5 Estudiantes
2. Ingresar nota de cada estudiante
3. Mostrar la mayor nota y de que estudiante es
4. Mostrar estudiantes y notas
5. Salir.
Digitar la opción a desarrollar: ''')
    match opcion:
        case '1':
            for i in range(0,5):
                nombresNotas[0].append(input(f"Digitar el nombre del alumno #{i+1}: "))
            paso1=True
        case '2':
            if(paso1 == True):
                for i in range(0,5):
                    notaInd = float(input(f"Digitar la nota de programación del alumno {nombresNotas[0][i]}: "))
                    while notaInd < 0.0 or notaInd > 5.0:
                        print("Error: Nota Invalida. Debe estar entre 0 a 5.")
                        notaInd = float(input(f"Digitar la nota de programación del alumno {nombresNotas[0][i]}: "))
                    nombresNotas[1].append(notaInd)
                paso2=True
            else:
                print("Error: Debe realizar el paso 1.")
        case '3':
            if(paso1 == True and paso2 == True):
                print(max(nombresNotas[1]))
                print(nombresNotas[1].index(max(nombresNotas[1])))
            else:
                print("Error: Debe realizar paso 1 y 2.")
        case '4':
            if(paso1 == True and paso2 == True):
                print("Nombres - Notas")
                for i in range(0,5):
                    print(f'''{nombresNotas[0][i]}: {nombresNotas[1][i]}''')
            else:
                print("Error: Debe realizar paso 1 y 2.")
        case '5':
            break
        case default:
            print("Error: Opción Invalida")