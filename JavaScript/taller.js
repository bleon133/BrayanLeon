//1.Desarrolle un algoritmo que permita leer 3 números enteros. El algoritmo debe imprimir cual es el numero mayor y cual es el numero menor entre los 3. Ademas ninguno de los 3 numeros ingresados pueden ser iguales. En caso de que el usuario ingrese 2 numeros iguales debe mostrar una alerta.
num1 = parseInt(prompt('Digitar el valor 1: '))
num2 = parseInt(prompt('Digitar el valor 2: '))
num3 = parseInt(prompt('Digitar el valor 3: '))
if(num1 > num2 && num1 > num3){
    alert(`El valor mayor es: ${num1}`)
}
else if(num2 > num1 && num2 > num3){
    alert(`El valor mayor es: ${num2}`)
}
else{
    alert(`El valor mayor es: ${num3}`)
}

//2.Desarrolle un algoritmo que reciba la base y altura de un triangulo en cm. Los 2 valores ingresados no pueden ser iguales, ademas el algoritmo debe calcular el area del triangulo si la base es mayor a 5cm y la altura es mayor a 4cm, si no lo son el algoritmo debe imprimir el valor de la base multiplicado por 2 y sumarle 10.
/* base = parseInt(prompt('Digitar la base (cm): '))
height = parseInt(prompt('Digitar la altura (cm): '))    
while(base == height){
    console.log('Error: Base y Altura tienen el mismo valor. Vuelve a digitarlo.')
    base = parseInt(prompt('Digitar la base (cm): '))
    height = parseInt(prompt('Digitar la altura (cm): '))   
}
if(base > 5 && height > 4){
    console.log(`El área es: ${(base*height)/2}`)
}
else{
    console.log(`El área es: ${(base*2)+10}`)
} */

//3.Desarrolle un algortimo que reciba un numero entero y escriba si dicho numero es par o impar.
/* num = parseInt(prompt('Digitar un valor: '))
if((num % 2) == 0){
    console.log(`El número ${num} es par.`)
}
else{
    console.log(`El número ${num} es impar.`)
} */

// 5.Desarrolle un algoritmo que permit convertir calificaciones numericas, segun la siguiente tabla:
// A = 19 y 20.
// B = 16, 17 y 18.
// C = 13, 14 y 15. 
// D = 10, 11 y 12.
// E = 1 hasta 9.
/* grades = parseInt(prompt('Digitar la nota del alumno: '))
while(grades < 1 || grades > 20){
    console.log('Error: Nota fuera del rango (Entre 1 hasta 20).')
    grades = parseInt(prompt('Digitar la nota del alumno: '))
}
if(grades >= 19 && grades <= 20){
    console.log('A')
}
else if(grades >= 16 && grades <= 18){
    console.log('B')
}
else if(grades >= 13 && grades <= 15){
    console.log('C')
}
else if(grades >= 10 && grades <= 12){
    console.log('D')
}
else{
    console.log('E')
} */