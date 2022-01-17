from re import X
from tkinter import Y

class deber:
    #Decidir si un numero es primo o no
    def ejercicio27 (self):
        def primo(numero):
            for i in range(2,numero):
                if numero%i==0:
                    return False
                return True
    numero=int(input("numero: "))
    if primo(numero): 
        print("es primo")
    else: 
        print("no es primo")
    #Realizar un programa que pida numeros al usuario, muiestre el factorial
    #de cada uno y luego la cantidad totalde numeros leidos.
    def ejercicio1 (self):
        def factorial():
            cantidad=0
            n=int(input("Numeros:"))
            while n!=-1:
                f=1
                if n!=0:
                    for i in range(1,n+1):
                        f=f*i
                print("factorial", f)
                cantidad+=1
                n=int(input("Numero: "))
                return cantidad
    #Realizar un programa que pida numeros positivos al usuario
    #muestre el numero cuya sumatoria de digitos fue mayor, y la cantidad de numeros
    #cuya sumatoria de digitos fue menor que 10.
    def ejercicio28 (self):
        cantidad=0
        mayor=-1
        numero=int(input("numero positivo:"))
        while numero>=0:
            sumaDigitos(numero)
            if sumaDigitos > mayor:
                mayor=sumaDigitos
                n_mayorsuma=numero
            if sumaDigitos < 10:
                cantidad+=1
                numero=int(input("numero positivo: "))
            print("sumatoria de digitos de",n mayorsuma,":",mayor)
            print("cantidad con sumatoria menor a 10:", cantidad)
    #Determine cual es la salida en pantalla si se ingresan los valores x=6, y=7:
    def ejercicio29 (self):
        def coordenadaZ(x,y):
            x=x+10
            y=y+15
            return x+y
        x=int(input("coordenada eje x:"))
        y=int(input("coordenada eje y:"))
        for i in range(3):
            z=coordenadaZ(x,y)
            x=x+1
            y=y+1
            print(x,".",y)
    #En el siguiente programa se debera imprimir el numero 2 si se le ingresan
    #como valores x=5, y=1.
    def ejercicio1 (self):
        def maximo(a,b):
            if x>y:
                return X
            else:
                return Y
        def minimo(a,b):
            if x<y:
                return X
            else:
                return Y
        x=int(input("un numero:"))
        y=int(input("otro numero:"))
        print(maximo(x-3, minimo(x+2, y-5)))     
    #Escribir una funcion que, dado un numero de DNI, retorne True si el numero
    #es valido y False si no lo es. Para que un numero de DNI sea valido debe tener entre
    #7 y 8 digitos.
    def ejercicio30 (self):
        def DNIvalido(dni):
            cantidad=0
            while dni!=0:
                cantidad=cantidad+1
                dni=dni//10
                return cantidad==7 or cantidad==0
    #Escribir una funcion que, dado un string, retorne la longitud de la
    #ultima palabra. Se considera que las palabras estan separadas por uno o mas espacios
    #Tambien podria haber espacios al principio o al final del string pasado por parametro.
    def ejercicio1 (self):
        def lenUltimaPalabra(frase):
            if len(frase)==0:
                return 0
            cantidad=0
            for i in range(len(frase)):
                if frase[i]!=' ':
                    cantidad+=1
                else:
                    if i<len(frase)-1 and frase[i+1]!=' ':
                        cantidad=0
                        return cantidad
    #Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
    #Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
    #Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
    #Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI.
    def ejercicio31 (self):
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud==0:
                return 0
            cantidad=0
            for i in range(longitud):
                if cadena[i]!=' ':
                    cantidad+=1
                else:
                    if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                        cantidad=0
                        return cantidad
                    def DNIvalido(dni):
                        cantidad=0
                        while dni!=0:
                            cantidad+=1
                            dni//=10
                            return cantidad==7 or cantidad==8
                        def primerosTresDigitos(numero):
                            while numero >= 1000:
                                numero = numero // 10
                                return numero
                            def obtenerIdentificador(nombre, dni):
                                nombre=nombre.strip()
                                id=nombre[:nombre.find(" ")]
                                id=id+str(lenUltimaPalabra(nombre))
                                id=id+str(primerosTresDigitos(dni))
                                return id
    #Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la 
    #primera letra de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados 
    #los demás caracteres. Precondición: el separador de palabras es el espacio: " ". 
    #Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor 
    #esperado ante distintos argumentos.
    def ejercicio32 (self):
        def titulo(cadena):
            def titulo(cadena):
                '''
                Recibe una cadena de caracteres y retorna una copia que tiene la
                primera letra de cada palabra en mayúsculas y el resto de las letras
                en minúsculas.
                >>> titulo('esto es una frase')
                'Esto Es Una Frase'
                >>> titulo('ESTO ES UNA FRASE')
                'Esto Es Una Frase'
                >>> titulo('palabra')
                'Palabra'
                >>> titulo('   esto es una frase')
                '   Esto Es Una Frase'
                >>> titulo('esto es una frase   ')
                'Esto Es Una Frase   '
                >>> titulo('esto   es   una   frase')
                'Esto   Es   Una   Frase'
                >>> titulo('')
                ''
                >>> titulo(' ')
                ' '
                >>> titulo('123')
                '123'
                >>> titulo('-1esto 2es 3una 4frase')
                '-1Esto 2Es 3Una 4Frase'
                >>> titulo('esto1 es2 una3 frase4---')
                'Esto1 Es2 Una3 Frase4---'
                '''
            nueva=""
            inicioPalabra=True              #indica el inicio de una palabra
            for caracter in cadena:
                if not caracter.isalpha():
                    nueva=nueva+caracter
                    inicioPalabra=True
                else:
                    if inicioPalabra:
                        nueva=nueva+caracter.upper()
                        inicioPalabra=False  #ya no es el inicio de una palabra 
                    else:
                        nueva=nueva+caracter.lower()
        return nueva
    #Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
    #B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
    #C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
    #D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
    #E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
    def ejercicio33 (self):
         def sumatoria(lista):
        suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#A
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#B
print("Sumatoria de los números:", sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#C
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")
    #Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
    #-Agregar pasajeros a la lista de viajeros.
    #-Agregar ciudades a la lista de ciudades.
    #-Dado el DNI de un pasajero, ver a qué ciudad viaja.
    #-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
    #-Dado el DNI de un pasajero, ver a qué país viaja.
    #-Dado un país, mostrar cuántos pasajeros viajan a ese país.
    #-Salir del programa.
    def ejercicio34 (self):
         def agregarPasajeros(pasajeros):
        nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

#programa principal
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")
    #Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
    #- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
    #- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    #-Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
    def ejercicio35 (self):
        def cargarNombres(alumnos):
       nombre=input("Nombre: ")
    while nombre!="x":
       alumnos.add(nombre)
       nombre=input("Nombre: ")
    return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)
   #Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
   #[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
   #Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
   def ejercicio36 (self):
       def direcciones(ventas):
            domicilios=set()
            for venta in ventas:
                domicilios.add(venta[3])
            return domicilios
    #Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: "r":5, "%":3, "a":8, "9":1.
    #¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?
    def ejercicio37 (self):
    contadores={}
    for i in range(50):
        cadena=input("Cadena de caracteres: ")
        for caracter in cadena:
            if caracter not in contadores:
                contadores[caracter]=1
            else:
                contadores[caracter]+=1
    print("Frecuencia de cada carácter")
    for caracter, cantidad in contadores.items():
        print(caracter, ": ", cantidad)</code></pre>

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
print("Frecuencia de cada letra")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)
   #Crear un programa para gestionar datos de los socios de un club, permitiendo:
   #-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
   #Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
   #Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
   #Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
   #-Informar cantidad de socios del club.
   #-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
   #-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
   #-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
   #-Imprimir el listado de socios completo.
   def ejercicio38 (self):
       def cargarSocios(socios):
        numero=int(input("Número de socio (0 para cortar): "))
          while numero!=0:
            nombre=input("Nombre y apellido: ")
            fecha=input("Fecha de ingreso (DDMMAAAA): ")
            cuota=input("¿Cuota al día? s/n: ")
            socios[numero]=[nombre,fecha,cuota.lower()=="s"]
            numero=int(input("Número de socio (0 para cortar): "))
   return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
   for numero,datos in socios.items():
       print("-Número:",numero)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formatoFecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

imprimirListado(socios_activos)
    #Crear un programa donde acceda por nombre de variablese existentes a los datos de una lista
    def ejercicio39 (self):
        def cargardatos(diccionario):
            dni=int(input("dni:"))
            while dni!=0:
                nombre=input("nombre:")
                domicilio=input("domicilio:")
                telefono=int(input("telefono:"))
                diccionario(dni)=(nombre,domicilio,telefono)
                dni=int(input("dni:"))
            return diccionario
        def imprimirdatos(diccionario):
            for clave, valor in diccionario.items():
                print(dni, nombre, domicilio, telefono)
                
                
                
                
                
                
tarea = deber()
#tarea.ejercicio27()
#tarea.ejercicio28()
#tarea.ejercicio29()
#tarea.ejercicio30()
#tarea.ejercicio31()
#tarea.ejercicio32()
#tarea.ejercicio33()
#tarea.ejercicio34()
#tarea.ejercicio35()
#tarea.ejercicio36()
#tarea.ejercicio37()
#tarea.ejercicio38()
#tarea.ejercicio39()
