""" print("Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables num1, num2, num3 respectivamente. El algoritmo debe imprimir cual es el mayor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos")
num1 = float(input("Digite el valor num 1 (debe ser diferente a los demás): "))
num2 = float(input("Digite el valor num 2 (debe ser diferente a los demás): "))
num3 = float(input("Digite el valor num 3 (debe ser diferente a los demás): "))
if(num1 != num2 and num1 != num3 and num2 != num3):
    if(num1 > num2 and num1 > num3):
        print(f"EL número mayor es: {num1}")
    elif(num2 > num1 and num2 > num3):
        print(f"EL número mayor es: {num2}")
    elif(num3 > num1 and num3 > num2):
        print(f"EL número mayor es: {num3}")
    else:
        print("Error")
else:
    print("Los 3 valores deben ser diferentes.") """
""" print("Se pide leer tres notas del estudiante y calcular su definitiva en un rango de 0-5 y mostrar un mensaje donde diga si el estudiante aprobó o reprobó. Para que un estudiante apruebe debe haber obtenido un promedio de 3.0 en adelante. SI alguna nota esta fuera del rango, indicar que hay un error.")
nota1= float(input("Digite la primera nota: "))
nota2= float(input("Digite la segunda nota: "))
nota3= float(input("Digite la tercera nota: "))
promedio= 0.0
if((nota1>= 0.0 and nota1<= 5.0) and (nota2>= 0.0 and nota2<= 5.0) and (nota3>= 0.0 and nota3<= 5.0)):
    promedio= (nota1 + nota2 + nota3)/3
    if(promedio >= 3.0):
        print(f"El estudiante aprobo con un promedio de: {promedio}")
    else:
        print(f"El estudiante reprobó con un promedio de: {promedio}")
else:
    print("Error: Alguna nota esta fuera del rango") """
""" print("Dados dos números enteros, se desea saber si alguno de ellos es múltiplo del otro")
num1 = int(input("Digite el primer valor (debe ser en entero): "))
num2 = int(input("Digite el primer valor (debe ser en entero): "))
if((num1%num2) == 0):
    print(f"El valor {num1} es múltiplo de {num2}.")
elif((num2%num1) == 0):
    print(f"El valor {num2} es múltiplo de {num1}.")
else:
    print("Ninguno de los valores es múltiplo del otro.") """

""" examFinal,notaFinal,habilitacion= 0.0,0.0,0.0
par1= float(input("Digitar la nota de Parcial 1: "))
par2= float(input("Digitar la nota de Parcial 2: "))
if((par1 >= 0 and par1 <= 5.0) and (par2 >= 0 and par2 <= 5.0)):
    if((par1+par2)/2 >= 2.0):
        examFinal= float(input("Digitar la nota del Examen Final: "))
        if(examFinal >= 0 and examFinal <= 5.0):
            if(examFinal >= 2.0):
                notaFinal= (par1*30/100) + (par2*30/100) + (examFinal*40/100)
                if(notaFinal < 3.0 and notaFinal >= 2.0):
                    print(f"El estudiante reprobó con una nota final de: {notaFinal}, pero al ser igual o mayor a 2.0 el estudiante puede presentar habilitación")
                    habilitacion= float(input("Digitar la nota de la habilitación: "))
                    if(habilitacion >= 0 and habilitacion <= 5.0):
                        notaFinal= habilitacion
                    else:
                        print("Error: Valor erroneo en la nota, debe ser entre 0 a 5")
            else:
                notaFinal=examFinal
        else:
            print("Error: Valor erroneo en la nota, debe ser entre 0 a 5")
    else:
        notaFinal = (par1+par2)/2
        print(f"Nota Final: {(par1+par2)/2}. Reprobó la materia por bajo promedio.")
else:
    print("Error: Valores erroneos en las notas, debe ser entre 0 a 5")
if(notaFinal >= 3.0):
    print(f"El estudiante aprobó con una nota final de: {notaFinal}")
else:
    print(f"El estudiante reprobó con una nota final de: {notaFinal}") """
print("Leer 3 números diferentes y ordenarlos de menor a mayor.")
num1 = int(input("Digitar número 1 (Entero): "))
num2 = int(input("Digitar número 2 (Entero): "))
num3 = int(input("Digitar número 3 (Entero): "))
if(num1 > num2 and num1 > num3):
    if(num2 > num3):
        print(f"El orden es: {num1}, {num2} y {num3}")
    else:
        print(f"El orden es: {num1}, {num3} y {num2}")
elif(num2 > num1 and num2 > num3):
    if(num1 > num3):
        print(f"El orden es: {num2}, {num1} y {num3}")
    else:
        print(f"El orden es: {num2}, {num3} y {num1}")
elif(num3 > num1 and num3 > num2):
    if(num1 > num2):
        print(f"El orden es: {num3}, {num1} y {num2}")
    else:
        print(f"El orden es: {num3}, {num2} y {num1}")
else:
    print("Error")