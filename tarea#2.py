
numero1_como_cadena = input("Escribe un número: ")
numero2_como_cadena = input("Escribe el otro número: ")
# convertir a flotantes
numero1 = float(numero1_como_cadena)
numero2 = float(numero2_como_cadena)

if (numero1 < 0 and numero2 > 0) or (numero2 < 0 and numero1 > 0):
    resta = numero1 - numero2
    print("La resta es: {}".format(resta))
# Si ambos son negativos
elif numero1 < 0 and numero2 < 0:
    multiplicacion = numero1 * numero2
    print("El producto es: {}".format(multiplicacion))
# Si son distintos
elif numero1 != numero2:
    suma = numero1 + numero2
    print("La suma es: {}".format(suma))

#
suma = 10 + 5 + 7
resta = 10 - 5 - 7
multiplicacion = 10 * 5 * 7
division = 10 / 5 / 7
print("Suma: " , suma ,  "\nResta: " , resta , "\nMultiplicación: " , multiplicacion , "\nDivisión: " , division)
#ejercicio 3
a=float(input("Primer número:"))
b=int(input("Segundo número:"))
c=a+b
print("El resultado de la suma es", c)


#ejercicio4
n1=int(input("Ingresá un número:"))
n2=int(input("Ingresá otro número:"))
suma=n1+n2
print("Suman:", suma)
n3=int(input("Ingresá un nuevo número:"))
print("Multiplicación de la suma por el último número:",suma*n3)

#5
frase="Estoy programando"
print(frase[0])
i=6
print(frase[i])


#6
cadena=input("Ingresá una frase:")
longitud=len(cadena)
print(longitud%2 == 0)

#7
lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("Introduce un número en la lista:"))
for numero in lista:
	print(numero," ",end="")

#8
def f(x: int)->bool:
    print('f:', x)
    return True

def g(x: int)->bool:
    print('g:', x)
    return False

#9
print("Caso 1 - f or f or f :")
print(f(1) or f(2) or f(3))

print("Caso 2 - f or f or g :")
print(f(1) or f(2) or g(3))

print("Caso 3 - g or f or g :")
print(g(1) or f(2) or g(3))

print("Caso 4 - g or g or g :")
print(g(1) or g(2) or g(3))

#10
print("Caso 1:", not f(1) and f(2))
print(not f(1) and f(2))
print("Caso 2:", not g(1) and f(2))
print(not g(1) and f(2))
#11
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))


def imprimir_numeros_ascii(s):
  for i in s:
    print(ord(i))

s = input("Ingrese string")
imprimir_numeros_ascii(s)

#12
N=input("tu nombre:")
print("ahora estas en la matrix,  ",N)




costo=float(input("costo de la cena:$"))
servicio=costo*0.062
propina=costo*0.1
print("costo total de la comida:$ , costo+servicio+propina")


dia=int(input("dia de nacimiento:"))
mes=int(input("mes de tu nacimiento:"))
año=int(input("año de tu nacimiento:"))
print(dia,"/",mes,"/",año)

fecha=int(input("fecha en DDMMAA:"))
print(dia+"/"+mes+"/"+año)
año= fecha%1000
dia=fecha//100000
mes=(fecha//1000)%100
print(dia,"/",mes,"/",año)

capacidad=float(input("capacidad del tanque:"))
kmxl=float(input("rendimiento(km por litro):"))
rrecorido=float(input("km totales a rrecorer:"))
kmxtanque=capacidad*kmxl
print("seran necesarios",rrecorido/kmxtanque)


#ejercicio13

capacidadm2=4
porcentajegradas=0.2
porcentajespeciales=0.3
porcentajecomunes=0.7

dimensiones=float(input("dimensiones del estadio (en m2):"))
personasengradas=int(input("cantidad de personas que caben en las gradas:"))
porcentajeescenario=int(input("porcentaje que ocupa el escenario:"))
m2gradas=dimensiones*porcentajegradas
m2escenario=dimensiones*(porcentajeescenario/100)
m2disponibles=dimensiones-m2gradas-m2escenario
personastotales=(m2disponibles*4+personasengradas)
print("caben",personastotales,"personas")
precioentradacomun=float(input("precio entrada comun:"))
precioentradaespecial=float(input("precio entrada especial:"))
print("ingreso total de ventas":(personastotales*porcentajeesespeciales)*precioentradaespecial +
      (personastotales*porcentajecomunes)*precioentradacomun))


