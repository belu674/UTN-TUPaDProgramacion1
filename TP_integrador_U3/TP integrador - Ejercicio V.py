print("\nEscape Room: La Arena del Gladiador\n")

#Solicito el nombre del gladiador y valido que no sea vacio y solo contenga letras
while True:
    nombre_gladiador = input("Ingrese el nombre del Gladiador: ").upper()
    if nombre_gladiador.isalpha():
        break
    #Si no se cumple muestro un error y se solicita nuevamente
    print("Error: Solo se permiten letras.\n")

#Inicializo las variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True

#El while tiene como condicion que los dos participantes tengan vida > 0
while vida_gladiador > 0 and vida_enemigo > 0:
    print("----------RESUMEN DEL COMBATE----------")
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) VS Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")

    print("---------------MENÚ---------------")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar\n")

    #La opcion solo admite numeros, en caso de ingresar otra cosa se le muestra un mensaje de error y se pide que lo ingrese correctamente
    while turno_gladiador:
        opcion = input("Elija una opción: ")
        #Si la opcion no es un número devuelvo un error y vuelve al while para solicitarla nuevamente
        if opcion.isdigit():
            break
        print("Error: ingrese un número válido\n")
    
    if opcion == "1":
        if vida_enemigo < 20:
            daño_final = daño_ataque_pesado * 1.5
            vida_enemigo -= daño_final
            print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!\n")
        #El enemigo ataca luego de cada acción del gladiador
        vida_gladiador -= daño_enemigo
        print("\n¡El enemigo te atacó por 12 puntos de daño!\n")
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!\n")
        for i in range (3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
        #El enemigo ataca luego de cada acción del gladiador
        vida_gladiador -= daño_enemigo
        print("\n¡El enemigo te atacó por 12 puntos de daño!\n")
    elif opcion == "3":
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
        elif pociones_vida == 0:
            print("¡No quedan pociones!\n")
        #El enemigo ataca luego de cada acción del gladiador
        vida_gladiador -= daño_enemigo
        print("\n¡El enemigo te atacó por 12 puntos de daño!\n")
    else:
        #Se valida que solo ingrese opciones entre 1 y 3
        print("Error: ingrese un número entre 1 y 3.\n")

#Cuando sale del While se evalúa si el gladiador resultó ganador o perdedor
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.\n")
else:
    print("DERROTA. Has caído en combate.\n")
