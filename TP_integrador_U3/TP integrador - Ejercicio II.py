print("\nAcceso al Campus y Menú Seguro\n")

#Defino las credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

#Inicializo los intentos
intento = 1

while intento <= 3:
    print(f"Intento {intento}/3")
    #Solicito al usuario el usuario y clave
    intento_usuario = input("Usuario: ")
    intento_clave = input("Clave: ")

    #Valido si coinciden con las credenciales fijas
    if intento_usuario != usuario_correcto or intento_clave != clave_correcta:
        #Si no coinciden voy a verificar qué mensaje darle de acuerdo al número de intentos
        if intento < 3:
            print("Error: credenciales inválidas.\n")
        else:
            print("Cuenta bloqueada")
        #Sumo el intento erróneo
        intento += 1
    else:
        print("Acceso concedido.\n")
        while True:
            print("-----------MENÚ-----------")
            print("1) Estado\n2) Cambiar clave\n3) Mensaje\n4) Salir\n")
            opcion = input("Elija una opción: ")
            #Si la opcion no es un número devuelvo un error y vuelve al while para solicitarla nuevamente
            if not opcion.isdigit():
                print("Error: ingrese un número válido.\n")
            else:
                #Como tengo varias opciones voy a utilizar el match case
                match opcion:
                    case "1":
                        print("Inscripto\n")
                    case "2":
                        nueva_clave = input("Nueva clave: ")
                        nueva_clave_conf = input("Confirme la nueva clave: ")
                        #Valido que la nueva clave tenga como mínimo 6 caracteres
                        if len(nueva_clave) >= 6:
                            #Valido que las claves sean iguales
                            if nueva_clave == nueva_clave_conf:
                                clave_correcta = nueva_clave
                                print("Clave actualizada correctamente.\n")
                            else:
                                print("Las claves ingresadas no coinciden.\n")
                        else:
                            print("Error: mínimo 6 caracteres.\n")
                    case "3":
                        print("El único fracaso real es dejar de intentar.\n")
                    case "4":
                        #Solo cuando elige esta opción sale del programa
                        print("¡Hasta luego!\n")
                        break
                    case _:
                        #Utilizo el default para cuando ingrese un número fuera del rango permitido
                        print("Error: opción fuera de rango.\n")
        #Si accedió correctamente pero no llegó a los 3 intentos tengo que utilizar el break para salir del bucle While
        break