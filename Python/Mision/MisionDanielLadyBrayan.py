paso1, paso2 = False,False
numInt,opcion,resultados,imc,nivelPeso = 0,-1,'',0.0,''
while opcion != 5:
    opcion = input('''1. Ingresar cantidad de familiares.
2. Ingresar datos de los familiares necesarios para realizar los cálculos.
3. Mostrar resultados.
4. Acerca de. (Muestra nombre del talento que desarrolló el ejercicio
5. Salir.
Digitar la opción a desarrollar: ''')
    match opcion:
        case '1':
            numInt = int(input("Digitar el número de integrantes: "))
            paso1 = True
            print("")
        case '2':
            if(paso1 == True):
                for i in range(1, numInt+1):
                    nombre = input(f"Ingrese nombre del Pariente #{i}: ")
                    parentesto = input(f"Ingrese el parentesto #{i}: ")
                    peso = float(input(f"Digitar el peso de {nombre} en Kg: "))
                    while peso < 0:
                        print("Error: Valor del peso invalido, por favor, vuelva a digitarlo.")
                        peso = float(input(f"Digitar el peso de {nombre} en Kg: "))
                    estatura = float(input(f"Digitar el estatura de {nombre} en Metros: "))
                    while estatura < 0 or estatura > 3.0:
                        print("Error: Valor de la estatura es invalido, por favor, vuelva a digitarlo. Recuerde que debe escribir en metros, no en cm.")
                        estatura = float(input(f"Digitar el estatura de {nombre} en Metros: "))
                    imc = peso/(estatura**2)
                    if(imc<=18.5):
                        nivelPeso = 'Bajo peso'
                    elif (imc>=18.5 and imc<=24.9):
                        nivelPeso = 'Peso normal'
                    elif (imc>=25 and imc<=28.9):
                        nivelPeso = 'Sobrepeso'
                    elif (imc>=29 and imc<=34.9):
                        nivelPeso = 'Obeso I'
                    else:
                        nivelPeso = 'Obeso II'
                    resultados = resultados + "Familiar #" + str(i) + "-> Nombre: " + nombre + ", Parentesco: " + parentesto + ", Nivel de Peso: " + nivelPeso + "." + "\n" 
                    print("")
                paso2 = True 
            else:
                print("Error: Se debe primero digitar el número de integrantes.")
                print("")
        case '3':
            if(paso1 == True and paso2 == True):
                if(i == numInt):
                    print(resultados)
                else:
                    print(f"Error: Por favor, llenar los datos de los familiares en la opción #2 ({i}) igual al número de integrantes digitados ({numInt}).")
                    print("")
            else:
                print("Error: Se debe realizar las opciones anteriores del menú.")
                print("")
        case '4':
            print('''Acerca de:
* Daniel Prada Monroy 
* Lady Katherine Quintero López
* Brayan Steven León Martinez

''')
        case '5':
            break
        case default:
            print('''Opción inválida
            ''')