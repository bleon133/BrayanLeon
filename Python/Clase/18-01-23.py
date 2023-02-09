""" for i in range(0,5,2):
    print(i) """
""" i=1
while i<=10:
    print(i+1) 
    i=i+2 """
""" numero=0
residuo=0
binario=''
numero= int(input("Escribe un número: "))
while numero >0:
    residuo=numero%2
    binario=str(residuo)+binario
    numero=numero//2
print(f'binario: {binario}') """
""" num= 0
sum= 0
num = int(input("Digite un número: "))
for i in range(0,num+1,1):
    sum=sum+i
print(f'sumatoria: {sum}') """
""" print("Pedir al usuario un número del 1 al 9 y mostrar la tabla de multiplicar de dicho número")
num= 0
num= int(input("Digite un número: "))
if(num >= 1 and num <=9):
    print(f"Tabla de Multiplicar del: {num}")
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
    print("Fin.")
else:
    print(f"Error: El rango debe ser de 1 a 9") """
""" for i in range(1,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print(' ') """
""" print("Realizar un programa que imprima 25 términs de la serie 1-22-33-44, etc.")
x=0
for i in range(25):
    x=x+11
    print(x)
print(' ')
y=0
while y<=25:
    print(11*y)
    y=y+1 """

""" print("Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8-16-24,etc")
x=1
mul=8
while mul <= 500:
    print(mul)
    mul = 8*x
    x = x +1
print(" ")
for i in range(8,500,8):
    print(i) """
""" print("Realizar un programa que muestre los números del 1 al 10 en orden inverso.")
for i in range(10,0,-1):
    print(i, end=', ') """
""" i=10
while i>0:
    print(i) 
    i-=1 """
""" num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))
if(num1 < num2):
    x=num1
    y=num2
elif(num1 > num2):
    x=num2
    y=num1
for i in range(x,y+1):
    if(i%2 == 0):
        print(i) """
""" num3 = int(input("Digite un número: "))
num4 = int(input("Digite un número: "))
x=0
y=0
if(num3 < num4):
    x=num3
    y=num4
elif(num3 > num4):
    x=num4
    y=num3
if(x!=y):
    while x <= y:
        if(x%2 == 0):
            print(x)
        x=x+1
else:
    print("Error: Los dos valores son iguales")"""
print("Dado 2 números, contar la cantidad de nḿeros pares que existen entre sí")
num3 = int(input("Digite un número: "))
num4 = int(input("Digite un número: "))
x=0
y=0
z=0
if(num3 < num4):
    x=num3
    y=num4
elif(num3 > num4):
    x=num4
    y=num3
if(x!=y):
    while x <= y:
        if(x%2 == 0):
            z=z+1
        x=x+1
    print(f"La cantidad de números pares es: {z}.")
else:
    print("Error: Los dos valores son iguales")
print(" ")
num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))
z=0
if(num1 < num2):
    x=num1
    y=num2
elif(num1 > num2):
    x=num2
    y=num1
if(x!=y):
    for i in range(x,y+1):
        if(i%2 == 0):
            z=z+1
    print(f"La cantidad de números pares es: {z}.")
else:
    print("Error: Los dos valores son iguales")