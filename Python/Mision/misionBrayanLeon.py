print('''Nombre: Brayan Steven León Martinez
Grupo: G5-6:00AM A 10:00AM
Misión: USO DE CONDICIONALES''')
finalNote= 0.0
exam1= float(input("Digitar la nota del primer examen: "))
exam2= float(input("Digitar la nota del segundo examen: "))
exam3= float(input("Digitar la nota del tercer examen: "))
work1= float(input("Digitar la nota del primer trabajo: "))
work2= float(input("Digitar la nota del segundo trabajo: "))
finalExam= float(input("Digitar la nota del examen final: "))
selfEva= float(input("Digitar la nota de la autoevaluación del estudiante: "))
heteroEva= float(input("Digitar la nota de la heteroevaluación del docente: "))
if((exam1 >= 0.0 and exam1 <= 5.0) and (exam2 >= 0.0 and exam2 <= 5.0) and (exam3 >= 0.0 and exam3 <= 5.0) and (work1 >= 0.0 and work1 <= 5.0) and (work2 >= 0.0 and work2 <= 5.0) and (finalExam >= 0.0 and finalExam <= 5.0) and (selfEva >= 0.0 and selfEva <= 5.0) and (heteroEva >= 0.0 and heteroEva <= 5.0)):
    finalNote= (((exam1 + exam2 + exam3)/3)*55/100) + (((work1 + work2)/2)*15/100) + (finalExam*20/100) + (((selfEva + heteroEva)/2)*10/100)
    if(finalNote >= 3.0):
        print(f'''Resultados:
* Aprobación: El estudiante Aprobó con un total de {finalNote}.''')
    else:
        print(f'''Resultados:
* Aprobación: El estudiante Reprobó con un total de {finalNote}.''')
    if(finalNote >= 4.7 and finalNote <= 5.0):
        print(f"* Nivel: Tras haber sacado el estudiante una nota de {finalNote}, por ende, su nivel fue de SUPERIOR.")
    elif(finalNote >= 4.0 and finalNote <= 4.6):
        print(f"* Nivel: Tras haber sacado el estudiante una nota de {finalNote}, por ende, su nivel fue de ALTO.")
    elif(finalNote >= 3.0 and finalNote <= 3.9):
        print(f"* Nivel: Tras haber sacado el estudiante una nota de {finalNote}, por ende, su nivel fue de BÁSICO.")
    elif(finalNote >= 2.0 and finalNote <= 2.9):
        print(f"* Nivel: Tras haber sacado el estudiante una nota de {finalNote}, por ende, su nivel fue de BAJO.")
    else:
        print(f"* Nivel: Tras haber sacado el estudiante una nota de {finalNote}, por ende, su nivel fue de MUY BAJO.")
else:
    print("Error: Alguna de las notas digitadas estan fuera del rango de 0 a 5.")
