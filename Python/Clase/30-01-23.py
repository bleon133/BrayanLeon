""" opcion,x,y = 0,0,0
flag1,flag2 = False,False
animals = []
while opcion != 5:
    opcion = input('''1. Ingresar 10 animales
2. Mostrar de manera alfabética los animales
3. Búsqueda por número (Entre 1 al 10)
4. Búsqueda por término
5. Salir.
Digitar la opción a desarrollar: ''')
    match opcion:
        case '1':
            for i in range(10):
                animals.append(input(f"Digitar el nombre del animal #{i+1}: "))
            flag1 = True
        case '2':
            if(flag1 == True):
                animals.sort()
                print(animals)
            flag2 = True
        case '3':
            if(flag1 == True and flag2 == True):
                x = int(input(f"Digitar el mínimo intervalo (Entre 1 al 9): "))
                while x > 9 or x < 1:
                    print("Error: Debe ser entre 1 al 9, para mostrar al menos un valor.")
                    x = int(input(f"Digitar el mínimo intervalo: "))
                y = int(input(f"Digitar el máximo intervalo: "))
                while y < x or y > 10:
                    print("Error: Debe ser mayor al mínimo y no superar el valor de 10")
                    y = int(input(f"Digitar el máximo intervalo: "))
                print(animals[x-1:y])
        case '4':
            animalIndividual = input("Búsqueda. Digitar el nombre que desea buscar: ") """

print("Dado el siguiente arreglo=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2], dar la opción al usuario de indicar un número a buscar y mostrar la posición en que se encuentra un número por primera vez y por última vez dentro del arreglo.")
arreglo = [1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
posiciones = []
x = int(input("Digitar un número que desea buscar: "))
for i in range (len(arreglo)):
    if arreglo[i]==x:
        posiciones.append(i)
if(len(posiciones) > 0):
    print(f'''Posición Inicial: {posiciones[0]}
    Posición Final: {posiciones[len(posiciones)-1]}''')
else:
    print("Valor no encontrado")

