print("\nEscape Room: La Bóveda\n")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#Solicito el nombre y valido que no sea vacio y solo contenga letras
while True:
    nombre_agente = input("Ingrese el nombre del agente: ")
    if nombre_agente.isalpha():
        break
    #Si no se cumple muestro un error y se solicita nuevamente
    print("Error: El nombre debe contener solo letras y no estar vacío.\n")

#Determino una variables booleana para las condiciones que deben cumplirse para que el juego continúe y la inicializo
condicion = True

#Inicializo el contador
cont_cerradura_forzada = 0

while condicion:
    print("----------ESTADO ACTUAL----------")
    print(f"Energía: {energia}\nTiempo: {tiempo}\nCerraduras abiertas: {cerraduras_abiertas}\nAlarma: {alarma}")

    print("---------------MENÚ---------------")
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar\n")

    opcion = input("Elija una opción: ")
    #Si la opcion no es un número devuelvo un error y vuelve al while para solicitarla nuevamente
    if not opcion.isdigit():
        print("Error: ingrese un número válido.\n")
    else:
        #Como tengo varias opciones voy a utilizar el match case
        match opcion:
            case "1":
                #Cuento la cantidad de veces que ingresa a la opcion 1
                cont_cerradura_forzada += 1

                energia -= 20
                tiempo -= 2

                #Si ingresa a esta opcion 3 o mas veces seguidas se activa la alarma
                if cont_cerradura_forzada >= 3:
                    alarma = True
                    print("LA ALARMA ESTA ACTIVA Y NO ES POSIBLE ABRIR LA CERRADURA\n")
                elif energia < 40 and not alarma:
                    while True:
                        #Si el numero_riesgo_alarma no es un número entre 1 y 3 devuelvo un error y vuelve al while para solicitarlo nuevamente
                        numero_riesgo_alarma = input("Riesgo de alarma! Ingrese un número entre 1 y 3: ")
                        if numero_riesgo_alarma.isdigit and (numero_riesgo_alarma == "1" or numero_riesgo_alarma == "2" or numero_riesgo_alarma == "3"):
                            if numero_riesgo_alarma == "3":
                                alarma = True
                                print("SE ACTIVÓ LA ALARMA\n")
                            break
                        print("Error: ingrese un número válido entre 1 y 3.\n")
                
                if alarma == False:
                    cerraduras_abiertas += 1
                    print("CERRADURA ABIERTA\n")
            case "2":
                #Si elige otra opcion que no sea 1 el contador deberìa volver a 0
                cont_cerradura_forzada = 0
                energia -= 10
                tiempo -= 3

                for i in range(4):
                    codigo_parcial += "A"
                    print(f"Progreso del hackeo: {codigo_parcial}")
                
                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("CERRADURA ABIERTA\n")
            case "3":
                #Si elige otra opcion que no sea 1 el contador deberìa volver a 0
                cont_cerradura_forzada = 0
                tiempo -= 1
                energia += 15

                #El maximo de energia posible es 100
                if energia > 100:
                    energia = 100
                #Si la alarma esta activa se resta energía
                if alarma:
                    energia -= 10
            #Utilizo el default para cuando elige una opcion fuera de rango
            case _:
                print("Error: opción fuera del rango disponible.\n")

    condicion_bloqueo = alarma and tiempo <= 3 and cerraduras_abiertas < 3
    if cerraduras_abiertas == 3:
        print("\nGANASTE! ABRISTE LA BÓVEDA\n")
    elif energia <= 0 or tiempo <= 0:
        print("\nPERDISTE! LA BÓVEDA SE ENCUENTRA CERRADA\n")
    elif condicion_bloqueo:
        print("\nPERDISTE! EL SISTEMA SE ENCUENTRA BLOQUEADO Y NO ES POSIBLE ABRIR LA BÓVEDA!\n")
    
    condicion = energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not condicion_bloqueo
