""" database = ['Pepito89','SuperMongui','Espernancacion'],['123456','password','qwerty123']
intention,position = 1,-1
flag = False
while intention != 4:
    print(f"Intento #{intention}")
    user = input('Usuario: ')
    password = input('Contraseña: ')
    intention += 1
    for i in range(len(database[0])):
        if(user == database[0][i-1]):
            position = database[0].index(user)     
            if(password == database[1][position]):
                intention = 4
                flag = True
                print("----¡Bienvenido!----")
                break
    if(flag == False):
        print("Error: Mala digitación en el usuario y/o contraseña")
if(flag == False):
    print("Error: Intente más tarde. Supero el limite de intentos.") """
x = 0
matriz =  []
for i in range(5):
    matriz.append([])
    for j in range(10):
        matriz[i].append((j+1)+(i*10))
print(matriz)