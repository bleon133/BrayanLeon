""" lista=[1,1,1,'a']
print(lista[:]) """

""" dias=['Domingo','Lunes','Martes','Miercoles','Miercoles','Jueves','Viernes','Sábado']
for i in dias:
    print(i)

cadena='Hola Mundo'
for i in cadena:
    print(i) """

""" #Método Indirecto
dias=['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sábado']
for i in range(1,7,2):
    print(dias[i])
print("")
for i in range(6,-1,-1):
    print(dias[i])
 """

""" matriz=['nota1','nota2','nota3'],[3.5,4.0,3.0]
for i in range(2):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print("") """

""" lista=[]
for i in range(10):
    # num = int(input("Digite número: "))
    # lista.append(num)
    lista.append(int(input("Digite número: ")))
print(lista) """

""" def saludar(name):
    print('Hola', name)
saludar('Pedro') """

def sumar(val1,val2):
    # suma=val1+val2
    return val1+val2
suma= sumar(15,9)
print(suma) 