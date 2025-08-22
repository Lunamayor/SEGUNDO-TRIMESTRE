print("CONTROL DE INVENTARIO SIMPLE")

productos=[]

print ("Producto 1")

name_p1= input("Ingresé el nombre del producto: ")
cat_p1= input("Ingresé la categoría del producto: ")
can_p1= int(input("Ingresé la cantidad del producto que hay: "))
pre_p1= float(input("Ingresé el precio del producto: "))

producto1= {"nombre":name_p1, "categoría": cat_p1,"cantidad en stock": can_p1, "precio unitario": pre_p1}

productos.append(producto1)

print ("Producto 2")

name_p2= input("Ingresé el nombre del producto: ")
cat_p2= input("Ingresé la categoría del producto: ")
can_p2= int(input("Ingresé la cantidad del producto que hay: "))
pre_p2= float(input("Ingresé el precio del producto: "))

producto2= {"nombre":name_p2, "categoría": cat_p2,"cantidad en stock": can_p2, "precio unitario": pre_p2}

productos.append(producto2)

print ("Producto 3")

name_p3= input("Ingresé el nombre del producto: ")
cat_p3= input("Ingresé la categoría del producto: ")
can_p3= int(input("Ingresé la cantidad del producto que hay: "))
pre_p3= float(input("Ingresé el precio del producto: "))

producto3= {"nombre":name_p3, "categoría": cat_p3,"cantidad en stock": can_p3, "precio unitario": pre_p3}

productos.append(producto3)

print ("Producto 4")

name_p4= input("Ingresé el nombre del producto: ")
cat_p4= input("Ingresé la categoría del producto: ")
can_p4= int(input("Ingresé la cantidad del producto que hay: "))
pre_p4= float(input("Ingresé el precio del producto: "))

producto4= {"nombre":name_p4, "categoría": cat_p4,"cantidad en stock": can_p4, "precio unitario": pre_p4}

productos.append(producto4)

print ("Producto 5")

name_p5= input("Ingresé el nombre del producto: ")
cat_p5= input("Ingresé la categoría del producto: ")
can_p5= int(input("Ingresé la cantidad del producto que hay: "))
pre_p5= float(input("Ingresé el precio del producto: "))

producto5= {"nombre":name_p1, "categoría": cat_p1,"cantidad en stock": can_p1, "precio unitario": pre_p1}

productos.append(producto5)

print("Reporte")

valores=[can_p1*pre_p1,can_p2*pre_p2,can_p3*pre_p3,can_p4*pre_p4, can_p5*pre_p5]

print(f"La lista de todos sus productos es: {productos}\n el precio del {producto1['nombre']} tine un valor de {valores[0]} \n el precio del {producto2['nombre']} tine un valor de {valores[1]} \n el precio del {producto3['nombre']} tine un valor de {valores[2]} \n el precio del {producto4['nombre']} tine un valor de {valores[3]} \n el precio del {producto5['nombre']} tine un valor de {valores[4]} \n el valor total de su inventario es: {sum(valores)}")