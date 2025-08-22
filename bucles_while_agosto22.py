#print dentro del bucle
num=int(input("ingresa el numero: "))
while num >0:
    print(f"{num}")
    num-=1
    print("termino el conteo, finish")

# #print fuera del bucle (mejor)
num=int(input("ingresa el numero: "))
while num >0:
    print(f"{num}")
    num-=1
print("termino el conteo, finish")

#-------------- bucle infinito de numero al multiplicar 
# numer =int(input("ingresa el numero de la tabla de multiplicar: "))
# i = 1 #iniciacion 
# print(f"\inicia el contador en 1{numer}: ")
# while 1<=10: #bucle que se repite mientras i sea menor o igual a 10 
#     print(f"{numer} * {i} = {numer * i}")
#     i+= 1

#--------- tabla de multiplicar
#multiplicar hasta el multiplicador 10

numer =int(input("ingresa el numero de la tabla de multiplicar: "))
i = 1 #iniciacion 
print(f"\ninicia el contador en 1{numer}: ")
while i<=10: #bucle que se repite mientras i sea menor o igual a 10 
    print(f"{numer} * {i} = {numer * i}")
    i+= 1

#----------------- EJEMPLO
#salimos de blucle cuando i es igual a 3
i = 1
while i<6:
    print(i)
    if i ==3:
        break
    i +=1

#---- ACTIVIDAD-EJERCICIO
x=int(input("ingresa el numero: "))
while True:
    x-=1
    print(x)
    if x ==0:
        break
print("fin del bucle")


#--------- infinitamente pero en negativo jsjjs
# x=int(input("ingresa el numero: "))
# while True:
#     x-=1
#     print(x)
#     if x ==0:
#         break
# print("fin del bucle")

#---------------- WHILE - ELSE
chance = 1
while chance <=3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("Ok lo conseguiste en el intento", chance)
        break
    chance +=1
else:
    print("Has agotado tus tres intentos")


