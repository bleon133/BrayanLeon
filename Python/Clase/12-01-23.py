print("Problema: Comisiones sobre las ventas efectuadas en el mes")
sueldoBase= float(input("Ingrese el valor de sueldo base: "))
valorVenta= float(input("Ingrese el valor total de las ventas realizadas en el mes: "))
comision= 0.0
if(valorVenta >= 1000000 and valorVenta <= 2000000):
    comision= 3.0
elif(valorVenta > 2000000 and valorVenta <= 5000000):
    comision= 5.0
elif(valorVenta > 5000000):
    comision= 8.0
elif(valorVenta < 1000000 and valorVenta >= 0):
    print("Al ser tan bajo el valor en venta, no recibe comisión")
else:
    print("Valor ingresado erroneo")
print(f'La comisión asignada es de: {comision}%, es decir, {valorVenta*comision/100}, por lo tanto el valor que recibirá total en el mes es de: {sueldoBase+(valorVenta*comision/100)}')
