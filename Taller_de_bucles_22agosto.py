#-----------------------------  TALLER DE BUCLES
# 1. pide al usuario numeros enteros y sumalo hasta q ingrese 0. luego muestra el total

total = 0
while True:
    numero1=int(input("usuario, ungrese un numero, obio entero: "))
    if numero1==0:
        break
    total +=numero1
    print(f"Ok la suma total seria {total}")
       
#2. crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente
contraseña= ""
while contraseña !="python123":
    contraseña =input("ingrese la contraseña: ")
    if contraseña !="python123":
        print("contraseña incorrect, vuelva a intentarlo")
    print("contraseña correcta")
#