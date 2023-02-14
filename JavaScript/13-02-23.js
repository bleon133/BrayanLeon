var option = -1
var num1 = +prompt('Digitar número 1: ')
var num2 = +prompt('Digitar número 2: ')
while(option != 5){
    option = prompt(`1. Sumar (+)
2. Restar (-)
3. Multiplicar (*)
4. Dividir (/)
5. Salir
Escribir la opción a operar: `)
    switch(option){
        case '1':
            alert((num1+num2).toFixed(2))
            break
        case '2':
            alert((num1-num2).toFixed(2))
            break
        case '3':
            alert((num1*num2).toFixed(2))
            break
        case '4':
            alert((num1/num2).toFixed(2))
            break
        case '5':
            break
        default:
            alert('Error: Opción Incorrecta.')
            break
    }
}

