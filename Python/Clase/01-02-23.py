""" matriz = []
listaY = []
listaX = []
x,n,m = 0,0,0
for i in range(4):
    matriz.append([])
    for j in range(6):
        x += 1
        matriz[i].append((x))
for y in range(len(matriz)):
    for x in range(len(matriz[y])):
        n = n + matriz[y][x]
    listaY.append(n)
    n = 0
for z in range(len(matriz[0])):
    for v in range(len(matriz)):
        m = m + matriz[v][z]
    listaX.append(m)
    m = 0
print(listaY)
print(listaX) """

n = int(input("Digitar la cantidad de nombres a escribir: "))
name = " "
names = []
for i in range(n):
    name = input(f"Escribir el nombre # {i+1}: ")
    names.append(name)
print(names)
names2 = sorted(names)  
print(names2)