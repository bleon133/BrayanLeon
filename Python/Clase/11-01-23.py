'''
EdadPepe= int(input("Edad de PepeJunior: "))
EdadAgripino= int(input("Edad de Agripino: "))
if(EdadPepe > EdadAgripino):
    if((EdadPepe-EdadAgripino)==2):
        if(EdadPepe == 22):
            print("PepeJunior y Agripino son hijos de Pepe")
        else:
            print("PepeJunior y Agripino NO son hijos de Pepe")
    else:
        print("PepeJunior y Agripino NO son hijos de Pepe")
else:
    print("PepeJunior y Agripino NO son hijos de Pepe")
'''
'''
print("Empresa La Generosa S.A -> Aumentos de sueldo")
salarioBasico= float(input("¿Cuanto es el valor del salario del trabajador: "))
aumento= 0.0
if(salarioBasico <= 800000):
    aumento= 10.0
elif(salarioBasico > 800000 and salarioBasico <= 1200000):
    aumento= 8.0
else:
    aumento= 5.0
print(f'El aumento fue del: {aumento}%, por lo tanto, el salario nuevo es: {salarioBasico+(salarioBasico*aumento/100)}')
'''
'''
print("Auxilio de Transporte")
salarioEmpleado= float(input("¿Cuanto es el salario del empleado?: "))
if(salarioEmpleado <=2320000):
    print("Tiene derecho a Auxilio de Transporte")
else:
    print("No tiene derecho a Auxilio de Transporte")
'''
'''
opcion= int(input("Digita opción: "))
match opcion:
    case 1:
        print("Opción 1")
    case 2:
        print("Opción 2")
    case default:
        print("Ninguna opción")
'''
""" val1= float(input("Digita el primer valor: "))
val2= float(input("Digita el segundo valor: "))
opCalculadora = (input('''1. Suma
2. Resta
3. Multiplicación
4. División
5. Conciente
6. Residuo
Elegir la opción de operación: '''))
match opCalculadora:
    case '1':
        print(val1+val2)
    case '2':
        print(val1-val2)
    case '3':
        print(val1*val2)
    case '4':
        if val2==0:
            print("No es posible dividir por cero")
        else:
            print(val1/val2)
    case '5':
        print(val1//val2)
    case '6':
        print(val1%val2)
    case default:
        print("Opción Incorrecta") """
factura= float(input("Digita el valor de la factura de luz a pagar sin el subsidio: "))
opEstracto= input('''a. Estrato 1
b. Estrato 2
c. Estrato 3
d. Estrato 4
Digita la opción de su estracto de vivienda: ''')
subsidio= 0.0
match opEstracto:
    case 'a':
        subsidio= 10
    case 'b':
        subsidio= 8
    case 'c':
        subsidio= 6
    case 'd':
        subsidio= 4
    case default:
        print("Opción Incorrecta")
print(f'El subsidio a aplicar es: {subsidio}%, por ende, el valor a pagar es: {factura-(factura*subsidio/100)}')