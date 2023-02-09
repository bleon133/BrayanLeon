paso1,paso2,paso4=False,False,False
acumulador=0
opcion=0
while opcion != 6:
    opcion= int(input('''
1. Ingresar el nombre de un estudiante
2. Ingresar las notas de un estudiante
3. Mostrar la nota definitiva de un estudiante
4. Mostrar si el estudiante aprueba o no la materia
5. Mostrar el nombre del estudiante, nota definitiva y si aprobó o no la materia
6. Salir
Digita una opción: '''))
    match opcion:
        case 1:
            nombre= input('Dite el nombre del estudiante: ')
            paso1=True
        case 2:
            if(paso1==True):
                for i in range(5):
                    nota= -1
                    while nota<0 or nota>5:
                        nota=float(input(f'Digita la nota {i+1}'))
                    acumulador+=nota
                definitiva= acumulador/5
                paso2=True
            else:
                print("Primero debes hacer el paso 1")
        case 3:
            if paso1==True and paso2==True:
                print(definitiva)
            else:
                print('Primero debes hacer el paso 1 y 2')
        case 4:
            if paso1== True and paso2==True:
                if definitiva >= 3.5:
                    print("Aprobó")
                    estado='aprobó'
                else:
                    print("reprobó")
                    estado='reprobó'
                paso4=True
            else:
                print('Primero debes hacer el paso 1, 2 y 3')
        case 5:
            if paso1==True and paso2==True and paso4==True:
                print(f'Nombre: {nombre}, Definitiva {definitiva} y {estado}')
            else:
                print('Primero debes hacer el paso 1, 2, 3 y 4.')
        case 6:
            break
        case default:
            print("Valor incorrecto")