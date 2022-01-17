class deber:
    #declar el n=1000 para saber si es el ganador 
    def ejercicio14(self):
        num=int(input("N.de cliente: "))
        if num==1000:
            print("Ganastes un premio ")
     #ingresar un numero para saber si es mayor o menor 
    def ejercicio1(self):
        a=int(input("Ingrese un numero 1: "))
        b=int(input("Ingrese un numero 2: "))
        if a<b:
            print("El primero es menor")
        elif b<a:
            print("El segundo es menor")
        else:
            print("Son igual")
     #solicitar al usuario un dia de la semana 
    def ejercicio2(self):
        dia=input("Dia de la semana: ")
        if dia=="lunes":
            print("oh, no!")
        elif dia=="viernes":
            print("¡ya casi!")
        elif dia=="sabado" or dia=="domingo":
            print("Ahora si se puede descansar")
        else:
            print("A esperar el fin de semana!")        
     #Escribir un programa que dado un numero entero, muestre su valor absoluto
    def ejercicio15(self):
        num=int(input("Numero: "))
        if num<0:
            num=num*-1
        print("El valor absoluto es", num)
     #Solicitar al usuario que ingrese nombre de dos personas las cuales se almacena
     #en dos variables imprimir si el nombre si conciden con las msmas letras
    def ejercicio1(self):
        nombre1=input("Ingrese nombre: ")
        nombre2=input("Ingrese nombre: ")
        indice_final_nombre1=len(nombre1)-1
        indice_final_nombre2=len(nombre2)-1
        if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[indice_final_nombre2] :
            print("cincidencia")
        else:
            print("No hay concidencia") 
     #crear un progrma en el que el usuario le permita elegir un candidato
    def ejercicio2(self):
        candidato=input("Candidato elegido: ")
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo")
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido azul")
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido verde")
        else:
            print("Opcion erronea")    
     #Escribir un programa que solicite al usuario una letra y si es una vocal,
     #se debe validar que el usuario ingrese solo un caracter. Si ingresa un string
     #de mas informarle que no se puede procesar dato.       
    def ejercicio3(self):
        letra=input("Ingrese letra: ")
        if len(letra)!=1:
            print("Debe ser solo una letra")
        else:
            if letra.lower() in "aeiou":
                print("Es vocal")
            else:
                print("No es vocal")
     #hacer un programa que permita saber si un año es bisiesto.
     #para ser un año sea bisiesto debe ser divisible por 4 y no 
     #debe ser divisible por 100, excepto que tambien sea divisible por 400
    def ejercicio4(self):
        añio=int(input("Ingrese año: "))
        if añio %4 != 0:
            print("No es bisiesto.")
        else:
            if añio%100!=0 or añio%400 ==0:
                print("Es bisiesto")
            else:
                print("No es bisiesto")
     #Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. 
     # El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
     # Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. 
     # Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. 
     # Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
     # Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
     # Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
     # Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.
    def ejercicio16(self):
        fecha=input("Fecha (día, DD/MM'): ")
        fecha=fecha.lower()
        diasemana=fecha[0:fecha.find(',')]
        dianro=int(fecha[fecha.find(',')+2:fecha.find("/")])
        mesnro=int(fecha[fecha.find('/')+1:])
        if dianro>31 or mesnro>12:
          print("Fecha incorrecta")
        else:
            if diasemana in "lunes,martes,miércoles":
               respuesta=input("¿Se tomaron exámenes? S/N: ")
               if respuesta.lower()=="s":
                aprobados=int(input("Cantidad de aprobados: "))
                reprobados=int(input("Cantidad de reprobados: "))
                print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
            elif diasemana=="jueves":
                 asistencia=int(input("Porcentaje de asistencia: "))
                 if asistencia>50:
                    print("Asistió la mayoría")
                 else:
                    print("No asistió la mayoría")
            elif diasemana=="viernes":
                if dianro==1 and (mesnro==1 or mesnro==7):
                   print("Nuevo ciclo")
                alumnos=int(input("Cantidad de alumnos: "))
                arancel=float(input("Arancel: $"))
                print("Ingreso total: $", alumnos*arancel)
            else:
              print("Fecha incorrecta")
        print("Fin del programa")
     #ejercicios con estructura for   
    def ejercicio17(self):    
        # for x in range (10):
        #     print(x)
        # for x in range (100,200):
        #     print(x)
        # for x in range (5,20,3):
        #     print(x)
        # n=int(input("Ingrese numero: "))
        # for x in range(n,n*2):
        #     print(x)
        # c=int(input("Cantidad de numero: "))
        # total=0
        # for variable in range(c):
        #     numero=int(input("Numero a sumar: "))
        #     total=total+numero
        # print("total de la suma: ",total)
        frase=input("Frase: ")
        cantidad=0
        for x in frase:
            if x in "aeiou":
                cantidad+=1
        print("cantidad de vocales:", cantidad)
     #Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.
    def ejercicio18(self):
        total=0
        for i in range(101):
            if i%3 == 0:
             total+=i
        print("Sumatoria de los múltiplos de 3:", total)
     #Dado un número entero positivo, mostrar su factorial. 
     #El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.      
    def ejercicio1(self):
       numero=int(input("Número:"))
       f=1
       if numero!=0:
          for i in range(1,numero+1):
              f=f*i
       print("Factorial:", f) 
     #  Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
     #  La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es 
     #  la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…           
    def ejercicio2(self):
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
          n3=n1+n2
          print(n3)
          n1=n2
          n2=n3  
     #  Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
     #  Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
     # No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.    
    def ejercicio3(self):
        sumaNegativos=0            
        sumaPositivos=0
        cantidadPositivos=0
        for i in range(6):
            nro=int(input("Número: "))
            if nro>0:
               sumaPositivos=sumaPositivos+nro
               cantidadPositivos=cantidadPositivos+1
            else:
                sumaNegativos=sumaNegativos+nro
        print("Sumatoria de los negativos: ", sumaNegativos)
        if cantidadPositivos!=0:
           print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
        else:
           print("No se ingresaron números positivos")
     #Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. 
     # La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes.
     # Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. 
     # Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
     # Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. 
     # El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
     # Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. 
     # Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
     # Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
    def ejercicio19(self):
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        corrimiento=int(input("Corrimiento: "))
        for i in range(5):
            mensaje=input("Mensaje a encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                   indice=alfabeto.find(caracter.lower())
                   indice=(indice+corrimiento)%27
                   encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
            print("*** Mensaje encriptado: ", encriptado)
     #Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
     # Finalmente, mostrar la sumatoria de todos los números ingresados.       
    def ejercicio20(self):
        total=0
        nro=int(input("Número: "))
        while nro != 0:
            total+=nro
            nro=int(input("Número: "))
            print("Total:",total)
     #Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
     # Finalmente, mostrar la sumatoria de todos los números positivos ingresados.        
    def ejercicio1(self):
        positivos=0
        n=int(input("Número (0 para terminar): "))
        while n!=0:
              if n>0:
                positivos+=1
                n=int(input("Número (0 para terminar): "))
        print("Cantidad de positivos:", positivos)    
     # Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
     # Informar cuál fue el mayor número ingresado.  
    def ejercicio2(self):
        mayor=-1
        n=int(input("Número positivo:"))
        while n>=0:
            if n>mayor:
                mayor=n
                n=int(input("Número positivo:"))
        print("Mayor número ingresado:", mayor) 
     #Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.      
    def ejercicio3(self): 
         suma=0
         n=int(input("Número positivo:"))
         while n!=0:
            digito=n%10
            suma+=digito
            n=n//10
         print("Suma de los dígitos:", suma)
     # solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
     # La condición de corte es que se ingrese el número-1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares. 
    def ejercicio4(self):
        pares=0
        n=int(input("Número (-1 para terminar el programa): "))
        while n!=-1:
             if n%2 == 0:
               pares+=1
             suma=0
             while n!=0:
              digito=n%10
              suma+=digito
              n=n//10
             print("Suma de sus dígitos:", suma)
             n=int(input("Número (-1 para terminar el programa): "))
        print("Se ingresaron", pares, "números pares")
     #Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, 
     # la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
     # Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
     # Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.      
    def ejercicio21(self):
        total=0
        monto=float(input("Monto de una venta: $"))
        while monto!=0:
            if monto<0:
                print("Monto no válido.")
            else:
                  total+=monto
            monto=float(input("Monto de una venta: $"))
        if total>1000:
          total-=total*0.1
        print("Monto total a pagar: $", total)
     #Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
     # Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
     # Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.                    
    def ejercicio1(self):
        numero=int(input("numero: "))
        totalPares=0
        totalImpares=0
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:   
                ultimodigito=numero%10
                if ultimodigito%2==0:
                   pares+=1
                   totalPares+=1
                else:
                   impares+=1
                   totalImpares+=1
                numero=numero//10
            print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
            numero=int(input("Otro número: "))
        print("Total de dígitos pares:", totalPares)
        print("Total de dígitos impares:", totalImpares)
     # Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
     # Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
     # Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
     # **Ejemplo de ejecución:**
     # Libro: Los 3 mosqueteros
     # Libro: Historia de 2 ciudades
     # Libro: /
     # Línea completa. Aparecen 2 dígitos numéricos.
     # Libro: 20000 leguas de viaje submarino
     # Libro: El señor de los anillos
     # Libro: /
     # Línea completa. Aparecen 5 dígitos numéricos.
     # Libro: 20 años después
     # Libro: *
     # Fin. Se leyeron 2 líneas completas.  
    def ejercicio2(self):
        DigitosEnLaLinea=0
        Cantlineas=0
        titulo=input("Titulo del libro: ")
        while titulo!="*":
            if titulo=="/":
                Cantlineas+=1
                print("Linea completa. Aparecen", DigitosEnLaLinea,"digitos")
            else:
                for caracter in titulo:
                    DigitosEnLaLinea+=1
            titulo=input("Titulo del libro: ")
        print("fin. Se leyeron",Cantlineas,"lineas")
     #Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
     # Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
    def ejercicio22(self):
        frase=input("Frase: ")
        frase=input("Frase: ").strip()
        cantidad=0
        len_p_mas_larga=0
        while len(frase) != 0:
            cantidad=cantidad+1
            i=frase.find(" ")
            if i != -1:
               palabra=frase[0:i]
               while i < len(frase) and frase[i] == " ":
                     i=i+1
               frase=frase[i:]
            else:
               palabra=frase
               frase=""
            if len(palabra) > len_p_mas_larga:
               len_p_mas_larga=len(palabra)
               p_mas_larga=palabra
        if cantidad > 0:
           print("Palabra más larga:", p_mas_larga)
        print("Cantidad de palabras:", cantidad)           
     # Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
     # A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
     # El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
     # Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.    
    def ejercicio23(self):
        while True:
            print("Opción 1 - comenzar programa")
            print("Opción 2 - imprimir listado")
            print("Opción 3 - finalizar programa")
            opcion=int(input("Opción elegida: "))
            if opcion==1:
                print("¡Comenzamos!")
            elif opcion==2:
                 print("Listado:")
                 print("Nadia, Esteban, Mariela, Fernanda")
            elif opcion==3:
                 print("Hasta la próxima")
                 break
            else:
               print("Opción incorrecta. Debe ingresar 1, 2 o 3")             
     #Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
     # Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
     # Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
     # Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.   
    def ejercicio1(self):
        frase=input("Frase: ")
        l=input("Letra para buscar su posición: ")
        i=0
        while i!=len(frase):
            if l!=frase[i]:
               print("No se encontró en la posición", i)
               i+=1
               continue
            print("Se encontró en la posición", i)
            break
     #Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. 
     # Imprimir la cantidad de números primos ingresados.   
    def ejercicio24(self):
        cantidad=0
        n=int(input("Número: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                   primo=False
                   break
            if primo:
               cantidad+=1
            n=int(input("Número: "))
        print("primos: ", cantidad)
     #Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. 
     # Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.  
    def ejercicio1(self):
       añioInicio=int(input("Año inicial:"))
       añioFin=int(input("Año final:"))
       for añio in range(añioInicio, añioFin+1):
           if not añio%10==0:
             continue
           if not añio%4==0:
             continue
           if añio%100!=0 or añio%400==0:
              print(añio) 
     #Solicitar al usuario que ingrese su dirección email. 
     # Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
     # Una dirección se considerará válida si contiene el símbolo "@".
     #def ejercicio25(self):
       
# def validar(email):
#     caracterBuscado="@"
#     emailValido=False
#     for c in email:
#         if c==caracterBuscado:
#             return True
#     return False

# #programa principal
# direccion=input("Tu email: ")
# if validar(direccion):
#     print("Dirección válida")
# else:
#     print("Dirección inválida")
     # Solicitar números al usuario hasta que ingrese el cero. 
     # Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).   
    #def ejercicio26(self):
        
# def sumaDigitos(numero):
#     suma=0
#     while numero!=0:
#         digito=numero%10
#         suma=suma+digito
#         numero=numero//10
#     return suma
# sumatoria=0
# num=int(input("Número a procesar: "))
# while num!=0:
#     print("Suma:",sumaDigitos(num))
#     sumatoria=sumatoria+num
#     num=int(input("Número a procesar: "))
# print("Sumatoria:", sumatoria)
# print("Dígitos:", sumaDigitos(sumatoria))
# pass

def primo(num):
       for i in range(2,num):
           if num%i==0:           
              return False
           return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#programa principal
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))       
        
     
        



tarea = deber()
#tarea.ejercicio14()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio15()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio3()
#tarea.ejercicio4()
#tarea.ejercicio16()
#tarea.ejercicio17()
#tarea.ejercicio18()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio3()
#tarea.ejercicio19()
#tarea.ejercicio20()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio3()
#tarea.ejercicio4()
#tarea.ejercicio21()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio22()
#tarea.ejercicio23()
#tarea.ejercicio1()
#tarea.ejercicio24()
#tarea.ejercicio1()
#tarea.ejercicio25()
#tarea.ejercicio26()