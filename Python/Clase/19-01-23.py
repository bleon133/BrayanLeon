""" print("Algoritmo que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la media de todos ellos. Piensa como debemos inicializar las variables")
max= 0
min= 0
pro= 0
i= 1
actual= 1
anterior= 0
while actual !=0:
    actual = int(input("Digitar un número entero: "))
    if(i==1):
        anterior=actual
    elif(i==2):
        if(anterior>actual):
            max=anterior
            min=actual
        elif(anterior<actual):
            max=actual
            min=anterior
    elif(i > 0 and actual!=0):
        if(actual>max):
            max=actual
        elif(actual<min):
            min=actual
    if(actual!=0):
        pro=pro+actual
        i = i+1
pro=pro/(i-1)
print(f'''Resultados:
* Máximo: {max}
* Minimo: {min}
* Promedio: {pro}''') """

""" print("Mostrar los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el bucle que desees.")
print("Divisibles en 2 y 3:")
for i in range (1,101,1):
    if(i%2 == 0 and i%3 == 0):
        print(i, end=" ")
    i= i+1 """

print("Se desea validad una clave que sea 123456 hasta en tres oportunidades, debe indicar cuantos intentos lleva y cuantos le restan.")
clave= 0
i= 0
while clave != 123456 and i!=3:
    clave= int(input("Digitar la clave: "))
    if(clave != 123456):
        i=i+1
        print(f'''Clave Incorrecta.
Intentos Fallidos: {i}
Intentos Restantes: {3-i}''')
    else:
        print("Clave Correcta.")