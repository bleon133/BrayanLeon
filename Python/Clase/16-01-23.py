""" print("Bonificaciones por Tiempo de servicio y Estado Civil")
bonificacion= 0.0;
sueldo= float(input("Digitar el sueldo que gana: "))
timeService= input('''1. <= 5 años
2. >= 6 años y <= 10 años
3. > 10 años
Elegir el tiempo de servicio: ''')
estCivil= input('''1. Soltero
2. Casado
3. Ninguna de las anteriores
Elegir el estado civil: ''')
match estCivil:
    case '1':
        match timeService:
            case '1':
                bonificacion= 2
            case '2':
                bonificacion= 5
            case '3':
                bonificacion= 10
            case default:
                bonificacion= 0
    case '2':
        match timeService:
            case '1':
                bonificacion= 5
            case '2':
                bonificacion= 10
            case '3':
                bonificacion= 15
            case default:
                bonificacion= 0
    case '3':
        bonificacion= 0
if(bonificacion != 0):
    print(f'La bonificación a recibir es de: {sueldo*bonificacion/100}, por ende, el sueldo total es: {sueldo+(sueldo*bonificacion/100)}')
else:
    print("NO recibe bonificación, intente otra vez.") """

print("Conovatoria Profesional")
name= str(input("Digitar el nombre del usuario: "))
print('''Pregrado: Nivel de Tecnólogo o Profesional.
Posgrado: Nivel Especialista, Magister o Doctorado.''')
studies= input('''1. Solo pregrado
2. Solo posgrado
3. Pregrado y posgrado
4. Ninguna de las anteriores
Elegir el nivel de estudios obtenidos: ''')
match studies:
    case '1':
        age= int(input("Digitar la edad: "))
        if(age >= 25 and age <= 35):
            print(f"El candidato {name} SI es Apto para el puesto.")
        else:
            print(f"El candidato {name} NO es Apto para el puesto.")
    case '2':
        print(f"El candidato {name} SI es Apto para el puesto.")
    case '3':
        print(f"El candidato {name} SI es Apto para el puesto.")
    case '4':
        print(f"El candidato {name} No es Apto para el puesto.")

