print("\nCaja del Kiosco\n")


while True:
    #Solicito el nombre del cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    #Valido que el nombre del cliente no esté vacío y contenga solo letras
    if nombre_cliente.isalpha():
        #En caso de que se cumpla la condición voy a finalizar el While
        break
    #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realizará una nueva iteración del while para que lo ingrese correctamente
    print("Error: El nombre debe contener solo letras y no estar vacío.")

while True:
    #Solicito la cantidad de productos
    cantidad_productos = input("Ingrese la cantidad de productos que desea comprar: ")
    #Valido que el usuario ingrese caracteres númericos y, además, que sean enteros positivos.
    if cantidad_productos.isdigit() and int(cantidad_productos) > 0:
        #Convierto el string en entero
        cantidad_prod = int(cantidad_productos)
        #En caso de que se cumpla la condición voy a finalizar el While
        break
    #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realizará una nueva iteración del while para que lo ingrese correctamente
    print("Error: Ingrese un número entero positivo.")

#Inicializo las variables
precio_prod_total = 0
precio_total_descuento = 0.0
monto_ahorro = 0.0

for producto in range (cantidad_prod):
    while True:
        #Voy a solicitar el precio de cada producto
        precio_producto = input(f"Ingrese el precio del producto {producto + 1}: ")
        #Valido que el usuario ingrese caracteres númericos y, además, que sean enteros positivos. La consigna pide entero
        if precio_producto.isdigit() and int(precio_producto) > 0:
            #Convierto el string en entero
            precio_prod = int(precio_producto)
            #Voy a sumar el precio de cada producto que vaya ingresando el cliente en una variable
            precio_prod_total += precio_prod
            #En caso de que se cumpla la condición voy a finalizar el While
            break
        #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realiza una nueva iteración del while para que lo ingrese correctamente
        print("Error: Ingrese un número entero positivo.")
    
    while True:
        #Voy a solicitar que ingrese si el producto tiene descuento o no.
        descuento = input("Indique con S (si) o N (no) si el producto tiene descuento: ").lower()
        #Valido que el usuario cumpla lo solicitado. Solo valido la minúscula por el lower que aplique a la variable descuento.
        if descuento == "s" or descuento == "n":
            #En caso de que se cumpla la condición voy a finalizar el While
            break
        #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realiza una nueva iteración del while para que lo ingrese correctamente
        print("Error: Ingrese una opción válida")

    #Valido si el usuario eligió un producto con descuento
    if descuento == "s":
        #Aplico el 10% al precio del producto
        monto_descuento = precio_prod * 0.1
        #Calculo el precio del producto con el descuento aplicado
        precio_con_descuento = precio_prod - monto_descuento
        #Calculo el monto total del ahorro
        monto_ahorro += monto_descuento

    #Calculo el monto total con lo descuentos aplicados 
    precio_total_descuento = precio_prod_total - monto_ahorro

#Se imprime lo solicitado
print("-" * 25)
print(f"Total sin descuentos: ${precio_prod_total}")
print(f"Total con descuentos: ${precio_total_descuento:.2f}")
print(f"Ahorro: ${monto_ahorro:.2f}")
print(f"Promedio por producto: ${(precio_total_descuento / cantidad_prod):.2f}")
