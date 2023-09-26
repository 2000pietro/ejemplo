# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#EJERCICIO NUMERO 1-----------------------------------------------------
personas=4
pizza=5
rebanadas=8
rebTo=pizza*rebanadas
rebaxPe=2
rebCon=rebaxPe * personas
sobrante=rebTo - rebCon

print('el numero de rebandas sobrantes es: ') 

print(sobrante)

#EJERCICIO NUMERO 2-----------------------------------------------------
ca = 8
va=20
desc=0.2
pe = int(input('Ingresa el numero de camisetas que deseas: '))
total = pe*(va*desc)
print('El costo total de tu factura es: ', total)

#EJERCICIO NUMERO 3----------------------------------------------------

t = float(input('Ingrese el tiempo estimado: '))
d = float(input('Ingrese la distancia deseada: '))
x = d/t
print('La distancia recorrida en una hora es: \n ', x)

#EJERCICIO NUMERO 4------------------------------------------------------
ca = 15
cha = 50
desc = 0.1
p = (15 * 2)


#EJERCICIO NUMERO 5------------------------------------------------------
nPag = int(input('Ingresa el numero de paginas del libro: '))
nDias = int(input('¿En cuantos dias quiere leer el libro?: '))
nPagXDia = nPag/nDias
print('Numero de paginas a leer por dia: ', round(nPagXDia,0) )

#EJERCICIO NUMERO 6-----------------------------------------------------

costoCel=250
meses=int(input('¿En cuantos meses desea pagar el celular?: ',))
cuota=costoCel/meses
print('Cuota mensual de su celular es: ',round(cuota, 2), 'USD')

#EJERCICIO NUMERO 7------------------------------------------------------

viaje1 = 50
descEst = 0.15
est = int(input('Ingresa el numero de los pasajeros que son estudiantes: '))
total = viaje1 * descEst * est
print('Total a pagar de los estudiantes: ', total)

#EJERCICIO NUMERO 8------------------------------------------------------

porcion1 = 5
porcion2 = float(input('Numero de gramos que se desea cocinar: '))
paqFid1 = 500
paqFid2 = (porcion2 * paqFid1)/porcion1
print('Paquete que debe comprar: ', paqFid2)
print('Gramos de fideos que debe cocinar: ', paqFid2)

#EJERCICIO NUMERO 9-------------------------------------------------------

paq = 24
personas = float(input('Numero de personas: ')) 
galleTota = float(input(paq/personas))
print('A cada persona le corresponde: ', galleTota)

#EJERCICIO NUMERO 10------------------------------------------------------

cuenta = 200
dep = float(input('Ingresa el valor del deposito: '))
tiempoDep = int(input('Ingresa el numero de meses que desea visualizar en monto: '))
cuentaTotal = (dep * tiempoDep) + cuenta
print('Valor total de la cuenta despues de un año: ', cuentaTotal)

