#-----------------------------  TALLER DE BUCLES DE 15 PREGUNTAS ------------------------------------------------------------------
# 1. pide al usuario numeros enteros y sumalo hasta q ingrese 0. luego muestra el total

# total = 0
# while True:
#     numero1=int(input("usuario, ungrese un numero, obio entero: "))
#     if numero1==0:
#         break
#     total +=numero1
#     print(f"Ok la suma total seria {total}")
       
# 2. crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente
# contraseña= ""
# while contraseña !="python123":
#     contraseña =input("ingrese la contraseña: ")
#     if contraseña !="python123":
#         print("contraseña incorrecta, vuelva a intentarlo")
#     print("contraseña correcta")

# 3. #pide productos uno por uno y guardalos en una lista. termina cuando el usuario escrb "fin", luego muestra toda la lista 
# lista=[input("ingresa el primer producto: "),input("ingresa el primer producto: "), input("ingresa el segundo producto: "), input("ingresa el tercer producto: ")]



#4. Pide 10 números al usuario. Usa while para contarlos y guarda cuántos son pares y cuántos impares.
# pares = 0
# impares = 0
# cuenta = 0 
# while cuenta <=10:
#     numero= int(input("ingresa cualquier numero, sin miedo jsjs: "))
#     if numero % 2==0:
#         pares +=1
#     else:
#         impares +=1
#         cuenta +=1
# print(f"los numeros pares son {pares}, los impares son los {impares}")

#5. Pide al usuario ingresar notas entre 0 y 5 hasta que escriba "salir". Guarda las notas en una lista y muestra el promedio
# notas = []
# while True:
#     i= input("baby, lo q vas a hacer es ingresar uan nota entre 0 y 5 (o puedes escribir salir para fnalizar): ")
#     if i == "salir":
#         break 
#     nota= float(i)
#     if 0<=nota <=5:
#         notas.append(nota)
# print(notas)





#6. Pide un número y genera su tabla del 1 al 10 con while.
# numer =int(input("ingresa el numero de la tabla de multiplicar: "))
# i = 1 #iniciacion 
# print(f"\ninicia el contador en 1{numer}: ")
# while i<=10: #bucle que se repite mientras i sea menor o igual a 10 
#     print(f"{numer} * {i} = {numer * i}")
#     i+= 1

#7. El programa tiene un número secreto (ej. 17). El usuario tiene que adivinarlo. Con cada intento, el programa dice si es mayor o menor
numero_secreto= ""
while numero_secreto !="17":
    numero_secreto =input("ingrese la contraseña: ")
    if numero_secreto !="17":
        print("contraseña incorrecta, vuelva a intentarlo")
        break 
    elif numero_secreto >10:
        print("el numero es mayor")
    else:
        print ("numero mayor")
    print("contraseña imcorrecta")

#8. Crea una tupla con frutas. Usa while para pedirle al usuario que adivine frutas hasta que acierte una que esté en la tupla.

tupla1=("fresa","pera","mango","uva", "banano")
adivinar =""
while not adivinar:
    fruta=input("ingresa una fruta para ver si adivinas: ")
    if fruta in tupla1:
        print("correcto, Felicidades!!!!")
        break 
    else:
        print("prueba con otra fruta, tu puedes intentarlo de nuevo")

#9. Crea un diccionario con 5 palabras en español y su traducción al inglés. Usa while para que el usuario ingrese una palabra en español y muestre su traducción (si está).
diccionario= {"Ardilla" : "Squirrel",
              "Travieso" : "Mischievous",
              "Proveedor": "Purveyo",
              "Otorrinolaringólogo":"Otolaryngologist",
              "Anémona":"Anemone"}
while True:
    palabra=input("ingresa una palabra en español o solo di salir para terminar: ")
    if palabra =="salir":
        break
    if palabra in diccionario:
        traduccion = diccionario[palabra]
        print("la traduccion de {palabra} es {traduccion}")
    else:
        print("la palabra no esta en el listado, sorry")    


#10. Haz un menú dentro de un while para que el usuario elija:1.Sumar 2. Restar,3. Multiplicar 4. Dividir 5. Salir Luego realiza la operación con dos números ingresados
 
while True:
    print("selecciona una operacion: ")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    opcion= input(("opcion: "))
    if opcion =="5":
        break
    num1=int(input("ingrea el primer numero: "))
    num2=int(input("ingresa el segundo numero: "))
    if opcion == "1":
        print(f"el resultado: es {num1 + num2}")
    elif opcion == "2":
        print(f"el resultado: es {num1 - num2}")
    elif opcion == "3":
        print(f"el resultado: es {num1 * num2}")
    elif opcion == "4":
        if num2 !=0:
            print("resultado: {num1 / num2}")
        else:
            print("no se puede dividir")
    else:
        print("esta operacion no vale baby")
#11. Pide nombres y edades de personas y guárdalos en un diccionario. Detente cuando el usuario escriba "salir" como nombre. Luego muestra el diccionario completo
personas = {}
while True: 
    nombre = input("holis, ingresa el nombre del estudiante, o simplemente puedes colocar salir para terminar: ")
    if nombre == "salir":
        break
    edad = input("Ingresa la edad: ")
    personas[nombre] = edad
print("Registro de personas:", personas) 



#12. Crea una lista de 5 colores. Usa un bucle while para que el usuario escriba colores hasta encontrar uno que esté en la lista.
colores = ["rojo", "azul", "verde", "amarillo", "negro"]
while True:
    color = input("Escribe un color: ")
    if color in colores:
        print("Color encontrado:", color)
        break
        
#13. Pide un número y muestra sus potencias desde la 1 hasta la 5 con while.
numero = int(input("Ingresa un número: "))
i = 1
while i <= 5:
    print(numero, "^", i, "=", numero**i)
    i = i + 1

#14. Pide 5 números con while y guarda en una lista sus cuadrados. Al final, muestra la lista. 
cuadrados = []
i = 1
while i <= 5:
    num = int(input("Ingresa un número: "))
    cuadrados.append(num**2)
    i = i + 1
print("Lista de cuadrados:", cuadrados)

#15. Crea un programa que te deje registrar estudiantes con su nota final (nombre y nota)
estudiantes = {}
while True:
    nombre = input("Ingresa el nombre del estudiante (o 'fin' para terminar): ")
    if nombre == "fin":
        break
    nota = input("Ingresa la nota: ")
    estudiantes[nombre] = nota
print("Diccionario de estudiantes:", estudiantes)
 