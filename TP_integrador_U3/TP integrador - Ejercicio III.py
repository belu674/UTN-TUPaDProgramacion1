print("Agenda de Turnos con Nombres\n")

while True:
    #Solicito el nombre del operador
    nombre_operador = input("Nombre del operador: ")
    #Valido que el nombre del operador no esté vacío y contenga solo letras
    if nombre_operador.isalpha():
        break
    #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realizará una nueva iteración del while para que lo ingrese correctamente
    print("Error: El nombre debe contener solo letras y no estar vacío.\n")

#Inicializo las variables de los turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
        print("---------------MENÚ---------------")
        print("1. Reservar turno\n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema\n")
        opcion = input("Elija una opción: ")
        #Si la opcion no es un número devuelvo un error y vuelve al while para solicitarla nuevamente
        if not opcion.isdigit():
            print("Error: ingrese un número válido.\n")
        else:
            #Como tengo varias opciones voy a utilizar el match case
            match opcion:
                case "1":
                    #Solicito el día para la reserva
                    dia = input("Elija el día para reservar el turno 1 = Lunes, 2 = Martes: ")
                    #Valido que solo ingrese las opciones disponibles
                    if dia == "1" or dia == "2":
                        #Solicito el nombre del paciente
                        nombre_paciente = input("Nombre del paciente: ").upper()
                        #Valido que el nombre del paciente contenga solo letras y no este vacio
                        if not nombre_paciente.isalpha():
                            #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realizará una nueva iteración del while para que lo ingrese correctamente
                            print("Error: El nombre debe contener solo letras y no estar vacío.\n")
                        else:
                            if dia == "1":
                                #Valido que si el paciente tiene un turno asignado
                                if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente or lunes4 == nombre_paciente:
                                    print("Ya tiene un turno asignado\n")
                                #Valido si quedan turnos disponibles
                                elif lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                                    print("Lo sentimos. No hay turnos disponibles para ese día\n")
                                #Asigno el primer turno disponible al paciente
                                else:
                                    if lunes1 == "":
                                        lunes1 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                                    elif lunes2 == "":
                                        lunes2 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                                    elif lunes3 == "":
                                        lunes3 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                                    elif lunes4 == "":
                                        lunes4 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                            else:
                                if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                                    print("Ya tiene un turno asignado\n")
                                elif martes1 != "" and martes2 != "" and martes3 != "":
                                    print("Lo sentimos. No hay turnos disponibles para ese día\n")
                                else:
                                    if martes1 == "":
                                        martes1 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                                    elif martes2 == "":
                                        martes2 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                                    elif martes3 == "":
                                        martes3 = nombre_paciente
                                        print("El turno fue agendado correctamente.\n")
                    #Si elige un día fuera de rango
                    else:
                        print("Error: El día ingresado no es válido.\n")
                        
                case "2":
                    #Solicito el día para cancelar
                    dia = input("Elija el día del turno que desea cancelar 1 = Lunes, 2 = Martes: ")
                    if dia == "1" or dia == "2":
                        nombre_paciente = input("Nombre del paciente: ").upper()
                        if not nombre_paciente.isalpha():
                            #En caso de que no se cumpla la condición le voy a mostrar al usuario un error y se realizará una nueva iteración del while para que lo ingrese correctamente
                            print("Error: El nombre debe contener solo letras y no estar vacío.\n")
                        else:
                            #Busco por día si el paciente tiene un turno asignado en alguno de los días
                            if dia == "1":
                                if lunes1 == nombre_paciente:
                                    lunes1 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                elif lunes2 == nombre_paciente:
                                    lunes2 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                elif lunes3 == nombre_paciente:
                                    lunes3 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                elif lunes4 == nombre_paciente:
                                    lunes4 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                #Si no hay turno asignado con ese nombre informo al paciente
                                else:
                                    print("Lo sentimos. No hay turnos registrados a su nombre para ese día\n")
                            else:
                                if martes1 == nombre_paciente:
                                    martes1 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                elif martes2 == nombre_paciente:
                                    martes2 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                elif martes3 == nombre_paciente:
                                    martes3 = ""
                                    print("El turno fue cancelado correctamente.\n")
                                else:
                                    print("Lo sentimos. No hay turnos registrados a su nombre para ese día\n")
                    else:
                        print("Error: El día ingresado no es válido.\n")
                case "3":
                    dia = input("Elija el día para visualizar la agenda 1 = Lunes, 2 = Martes: ")
                    if dia == "1" or dia == "2":
                        #Uso un ternario
                        if dia == "1":
                            #Utilizo el ternario para simiplificar la expresion condicional if-else
                            print(f"Turno 1: {lunes1 if lunes1 != "" else "(libre)"}\nTurno 2: {lunes2 if lunes2 != "" else "(libre)"}\nTurno 3: {lunes3 if lunes3 != "" else "(libre)"}\nTurno 4: {lunes4 if lunes4 != "" else "(libre)"}\n")
                        else:
                            #Utilizo el ternario para simiplificar la expresion condicional if-else
                            print(f"Turno 1: {martes1 if martes1 != "" else "(libre)"}\nTurno 2: {martes2 if martes2 != "" else "(libre)"}\nTurno 3: {martes3 if martes3 != "" else "(libre)"}\n")
                    else:
                        print("Error: El día ingresado no es válido.\n")
                case "4":
                    print("---------Resumen general de turnos---------")
                    #Inicializo la variable
                    lunes_ocupados = 0
                    #Verifico si el dia esta ocupado y los voy sumando en la variable lunes_ocupados
                    if lunes1 != "":
                        lunes_ocupados += 1
                    if lunes2 != "":
                        lunes_ocupados += 1
                    if lunes3 != "":
                        lunes_ocupados += 1
                    if lunes4 != "":
                        lunes_ocupados += 1

                    martes_ocupados = 0
                    if martes1 != "":
                        martes_ocupados += 1
                    if martes2 != "":
                        martes_ocupados += 1
                    if martes3 != "":
                        martes_ocupados += 1

                    #Calculo los dias disponibles
                    lunes_disponibles = 4 - lunes_ocupados
                    martes_disponibles = 3 - martes_ocupados

                    print(f"LUNES\nTurnos Ocupados: {lunes_ocupados} \nTurnos Disponibles: {lunes_disponibles}\n")
                    print(f"MARTES\nTurnos Ocupados: {martes_ocupados} \nTurnos Disponibles: {martes_disponibles}\n")

                    if lunes_disponibles < martes_disponibles:
                        print("El día martes cuenta con mas turnos disponibles.\n")
                    elif lunes_disponibles == martes_disponibles:
                        print("Tienen la misma cantidad de turnos disponibles.\n")
                    else:
                        print("El día lunes cuenta con mas turnos disponibles.\n")
                case "5":
                    print("Sistema cerrado.\n")
                    #Utilizo el break para finalizar el While
                    break
                #Uso el default del match para indicar que la opcion esta fuera del rango
                case _:
                    print("Error: opción fuera del rango disponible.\n")
    
