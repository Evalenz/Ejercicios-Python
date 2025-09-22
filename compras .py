compras = [ ]
while True:
    producto = input ("Ingrese un producto (o 'salir' para terminar): ")
    if producto == "salir":
        break
    compras.append(producto)    
print ("Lista de compras:", compras)

