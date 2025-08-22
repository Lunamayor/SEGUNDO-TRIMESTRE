#-----------------------------TALLER, PRIMERA PARTE ES DE CONDICIONALES Y OPERACIONE MATEMÁTICAS----------------------
#  1. Verifica si un número es positivo, negativo o cero
# num = float(input("Ingresa un número: "))
# if num > 0:
#     print(f"{num} es positivo")
# elif num < 0:
#     print(f"{num} es negativo")
# else:
#     print(f"{num} es cero")

# # 2. Calcula el mayor de dos números ingresados
# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# if num1 > num2:
#     print(f"El mayor de los dos números es {num1}")
# else:
#     print(f"El mayor de los dos números es {num2}")

# # 3. Determina si un número es par o impar
# num = int(input("Ingresa un número: "))
# if num % 2 == 0:
#     print(f"{num} es un número par")
# else:
#     print(f"{num} es un número impar")

# # 4. Dado un número, verifica si está entre 10 y 20
# num = float(input("Ingresa un número: "))
# if 10 <= num <= 20:
#     print(f"{num} está entre 10 y 20")
# else:
#     print(f"{num} no está entre 10 y 20")

# # 5. Dados tres números, encuentra el mayor usando condicionales
# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# num3 = float(input("Ingresa el tercer número: "))
# if num1 >= num2 and num1 >= num3:
#     print(f"El mayor de los tres números es {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"El mayor de los tres números es {num2}")
# else:
#     print(f"El mayor de los tres números es {num3}")

# # 6. Calcula el precio final con un 10% de descuento si el total es mayor a $100
# precio = float(input("Ingresa el precio: "))
# if precio > 100:
#     precio_final = precio * 0.9
#     print(f"El precio final con el 10% de descuento es ${precio_final:.2f}")
# else:
#     print(f"El precio final es ${precio:.2f}")

# # 7. Verifica si una persona puede votar (mayor o igual a 18 años)
# edad = int(input("Ingresa tu edad: "))
# if edad >= 18:
#     print("Puedes votar")
# else:
#     print("No puedes votar")

# # 8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP
# precio = float(input("Ingresa el precio: "))
# tipo_cliente = input("Ingresa el tipo de cliente (VIP o normal): ")
# if tipo_cliente.upper() == "VIP":
#     precio_final = precio * 0.8
#     print(f"El precio final con el 20% de descuento es ${precio_final:.2f}")
# else:
#     print(f"El precio final es ${precio:.2f}")

# # 9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo
# num = int(input("Ingresa un número: "))
# if num % 5 == 0 and num % 3 == 0:
#     print(f"{num} es múltiplo de 5 y de 3 al mismo tiempo")
# else:
#     print(f"{num} no es múltiplo de 5 y de 3 al mismo tiempo")

# # 10. Dado un número, verifica si es divisible entre dos números dados
# num = int(input("Ingresa un número: "))
# div1 = int(input("Ingresa el primer divisor: "))
# div2 = int(input("Ingresa el segundo divisor: "))
# if num % div1 == 0 and num % div2 == 0:
#     print(f"{num} es divisible entre {div1} y {div2}")
# else:
#     print(f"{num} no es divisible entre {div1} y {div2}")



#-----------------------------TALLER, SEGUNDA PARTE ES DE Ejercicios con Listas (con condicionales)-----------------------
#11. Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10

# nums=[int(input("Ingresa el numero 1: ")), int(input("Ingresa el numero 2: ")), int(input("Ingresa el numero 3: ")), int(input("Ingresa el numero 4: ")), int(input("Ingresa el numero 5: "))]

# if nums [2] > 10:
#     print("mayor a 10")
# else:
#     print(" menor o igual a 10")

#12. Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.

lista = [3, 5, 7, 9]
if lista [0] == 7:
    print("esta en la lista")
elif lista [1] == 7:
    print("esta en la lista")
elif lista [2] == 7:
    print("esta en la lista")
elif lista [3] == 7:
    print("esta en la lista")
else:
    print("no esta en la lista")
# otra forma de hacer el 12
lista1 = [3, 5, 7, 9]
if 7 in lista1:
    print("esta en la lista")
else:
    print("no esta en la lista")

#13. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.
lista2 = [4, 6, 2, 8]
suma=lista2 [0] + lista2 [1]
if suma > 10:
    print("suma alta")
else: 
    print("suma baja")

# 14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.
lista3 =  ["Ana", "Luis", "Pedro", "Marta"]
ultimo= lista [-1]
if ultimo == "marta":
    print("nombre correcto")
else: 
    print("nombre diferente")

#15. Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
colores = [input("ingresa el primer color: "), input("ingresa el segundo color: "), input("ingresa el tercer color: ")]
if colores [1] == "azul":
    colores[1] = "azul"
    print(colores)

#-----------------------------TALLER, TERCERA PARTE ES DE Ejercicios con Tuplas (con condicionales)-----------------------
# 16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.
tupla1 = (5, 8, 12, 20)
if tupla1 [0] < tupla1 [-1]:
    print("orden ascendente")
else:
    print("orden descendente")

# 17. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.
tupla2 = (25, 32, 28)
if tupla2 [1] > tupla2[-1]:
    print("edad mayor a 30")
else: 
    print("edad menor o igual a 30")

# 18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.

tupla3 = (1, 2, 3)

lista = list(tupla3)
if lista[1] == 2:
    lista[1] = 10
tupla3 = tuple(lista)
print(tupla3)

# 19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra "Coordenada alta", si no, "Coordenada baja"
tupla = (4, 9)
if tupla[1] > 5:
    print("Coordenada alta")
else:
    print("Coordenada baja")

# 20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra "Tuplas iguales", si no, "Tuplas diferentes"
tupla1 = (3, 4)
tupla2 = (3, 5)
if tupla1 == tupla2:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")

# 21. Crea un diccionario con { "nombre" : "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra "Adulto", si no, muestra "Menor de edad"
persona = {"nombre": "Juan", "edad": 17}
if persona["edad"] >= 18:
    print("Adulto")
else:
    print("Menor de edad")

# 22. Crea un diccionario { "nombre": "Lucia", "edad": 20}. Si la edad es mayor a 18, cambia el valor de "edad" a 21. Luego muestra el diccionario
persona = {"nombre": "Lucia", "edad": 20}
if persona["edad"] > 18:
    persona["edad"] = 21
print(persona)

# 23. Crea un diccionario con { "nombre": "Carlos" }. Si la clave "ciudad" no existe, agrégala con el valor "Bogotá" y muestra el diccionario
persona = {"nombre": "Carlos"}
if "ciudad" not in persona:
    persona["ciudad"] = "Bogotá"
print(persona)

# 24. Dado el diccionario { "producto": "pan", "precio": 1200}, verifica si la clave "precio" existe. Si existe, muestra su valor, si no, muestra "No hay precio"
producto = {"producto": "pan", "precio": 1200}
if "precio" in producto:
    print(producto["precio"])
else:
    print("No hay precio")

# 25. Crea un diccionario con { "pan": 1200, "leche": 2000}. Si "pan" está en el diccionario, muestra su precio; si no, muestra "Producto no disponible"
productos = {"pan": 1200, "leche": 2000}
if "pan" in productos:
    print(productos["pan"])
else:
    print("Producto no disponible")