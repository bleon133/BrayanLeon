""" i, equi, isos, esca, lado1, lado2, lado3 = 1,0.0,0.0,0.0,1,1,1
while lado1!=0 or lado2!=0 or lado3!=0:
    lado1 = float(input((f"Digite el lado 1 del triángulo # {i}: ")))
    lado2 = float(input((f"Digite el lado 2 del triángulo # {i}: ")))
    lado3 = float(input((f"Digite el lado 3 del triángulo # {i}: ")))
    if(lado1!=0 and lado2!=0 and lado3!=0):
        if(lado1==lado2 and lado2==lado3 and lado3==lado1):
            print(f"El triángulo # {i} es equilátero.")
            equi+=1
        elif((lado1 == lado2 and lado3 != lado1) or (lado1 == lado3 and lado2 != lado1) or (lado2 == lado3 and lado1 != lado2)):
            print(f"El triángulo # {i} es isósceles.")
            isos+=1
        else:
            print(f"El triángulo # {i} es escaleno.")
            esca+=1
        i+=1
print(f'''Totales:
Equiláteros: {equi}
Isósceles: {isos}
Escaleno: {esca}''')
if(equi < isos and equi < esca and equi != isos and equi != esca):
    print("El tipo Equiláteros tiene menor cantidad.")
elif(isos < equi and isos < esca and isos != equi and isos != esca):
    print("El tipo isósceles tiene menor cantidad.")
elif(esca < equi and esca < isos and esca != equi and esca != isos):
    print("El tipo escaleno tiene menor cantidad.")
elif(equi == isos and equi < esca):
    print("El tipo equilátero e isósceles tiene igual cantidad y son los menores")
elif(isos == esca and isos < equi):
    print("El tipo isósceles y equiláteros tiene igual cantidad y son los menores")
elif(esca == equi and esca < isos):
    print("El tipo escaleno y equiláteros tiene igual cantidad y son los menores")
elif(equi == esca and equi < isos):
    print("El tipo equiláteros y escaleno tiene igual cantidad y son los menores")
elif(equi == isos and equi == esca):
    print("Los 3 tipos tiene igual cantidad.") """
""" x=''
for i  in range(1,6):
    x+=str(i)
    print(x) """

""" print("NO optimo, solo funciona pra 54321")
x=54321
y=44000
z=48889
print(x)
for i in range(1,5): 
    x= x-z
    z=z-y
    y=y/10
    print(x) """

""" x= '54321'
for i in range(5,0,-1):
    print(x[0:i]) """
""" x= '54321'
for i in range(len(x),0,-1):
    print(x[0:i]) """
dividendo = float(input("Digitar el dividendo: "))
divisor = float(input("Digitar el divisor: "))
cociente=dividendo
residuo=0
i = 0
if dividendo>divisor:
    while cociente >= divisor:
        cociente-=divisor
        i+=1
    print(f"Conciente: {i} y Residuo: {dividendo-(divisor*i)}")
else:
    print(f"Conciente: 0 y Residuo: {dividendo}")


    


