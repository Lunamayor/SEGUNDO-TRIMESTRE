# primer ejercicio multiplo de 7
while True:
  num=int(input("Ingresé un número: "))
  if num%7==0:
    print("EL NÚMERO ES DIVISIBLE ENTRE 7")
    break
  else:
    print("El NÚMERO NO ES DIVISIBLE ENTRE 7")

#segundo ejercicio
cotactos={}
continuar= True
while continuar:
  nombre=input("ingrese el nmbre d usuario ('salir') para terminar")
  if nombre == "salir":
    continuar=False
else:
  telefono=input("ingrese el nm de contacto: ")
  email=input("ingrese el email de contacto: ")

contactos=[nombre]={'telefono':telefono,
                    'email':email}
print(contactos)

#tercer ejercicio
saldo = 1000  

while saldo > 0:
    monto = float(input("Ingrese el monto a retirar: ")) #monto o como se diga esa cosa
    
    if monto > saldo:
        print("el Saldo insuficiente. Intente con un monto menor.")
    elif monto <= 0:
        print("Ingrese un monto positivo.")
    else:
        saldo -= monto
        print(f"Retirado: {monto}. Saldo restante: {saldo}.")

#cuarto ejercicio
suma_total = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma_total += numero

print(f"Suma total: {suma_total}")

#quinto ejercicio
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El número mayor es: {numero1}.")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}.")
else:
    print("Los números son iguales.")

#sexto ejercicio
total = 0

while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    
    if producto == "fin":
        break
    
    precio = float(input("Ingrese el precio del producto: "))
    total += precio

print(f"Total a pagar: {total}.")

#septimo ejercicio
monto_compra = float(input("Ingrese el monto de la compra: "))

if monto_compra > 100000:
    descuento = monto_compra * 0.10
    monto_final = monto_compra - descuento
    print(f"Descuento aplicado: {descuento}. Monto final: {monto_final}")
else:
    print(f"Monto final: {monto_compra}")


#octavo ejericio
numero = input("Ingrese un número: ")
suma_digitos = 0
indice = 0

while indice < len(numero):
    suma_digitos += int(numero[indice])
    indice += 1

print(f"Suma de los dígitos: {suma_digitos}")

#noveno ejercicio
palabras = []

while True:
    palabra = input("Ingrese una palabra: ")
    
    if palabra in palabras:
        break
    
    palabras.append(palabra)

#decimo ejercicio
contador = 0
mayor = 0

while contador < 3:
    numero = float(input("Ingrese un número: "))
    
    if contador == 0 or numero > mayor:
        mayor = numero
    
    contador += 1

print(f"El mayor de los tres números es: {mayor}")

#onceavo ejercicio
estudiante = {}
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    programa = input("Ingrese el programa del estudiante: ")
    estudiante['nombre'] = nombre
    estudiante['edad'] = edad
    estudiante['programa'] = programa
    break

#doceavo ejercicio
diccionario = {}

contador = 0

while contador < 5:
    palabra_ingles = input("Ingrese una palabra en inglés: ")
    traduccion_espanol = input("Ingrese su traducción al español: ")
    
    diccionario[palabra_ingles] = traduccion_espanol
    contador += 1

print(diccionario)

#trece ejercicio
numeros = []
contador = 0
suma_total = 0

while contador < 10:
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)
    suma_total += numero
    contador += 1

print(numeros)
print(f"Suma total: {suma_total}.")