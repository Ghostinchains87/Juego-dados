from os import system, path, sys
import pickle
import random
#Lista de jugadores y puntajes 
jugadores = []
puntaje_para_ganar = 5000
jugador_player = 0
puntaje1 = 0
puntaje2 = 0

#Funcion de menu y opcion cls para limpiar pantalla
def mostrar_menu():
    system("cls")
    print("1. Nueva Partida")
    print("2. Lista de jugadores")
    print("3. Maximo puntaje de todos los tiempos")
    print("4. Cambiar puntaje para ganar partidas")
    print("5. Guardar y Salir")
    print()

#Validador de opciones (que esten dentro de 1 y 5)
def pedir_opcion():
    opcion = input("Ingrese una opcion: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        mostrar_menu()
        print("Opcion invalida")
        opcion = input("Ingrese una opcion: ")
    return opcion

#Funcion de buscar jugador por nombre
def buscar_jugador(nom):
    pos = 0
    jugador = None
    while pos < len(jugadores) and jugador == None:
        jds = jugadores[pos]
        if jds["nombre"] == nom:
            jugador = jds
        pos += 1
    return jugador

#Funcion de creacion de nuevo jugador, con ingreso de nombre y guardandolo en la lista "nombre"
def nuevo_jugador():
    global jugador_player
    system("cls")
    nom = input("Ingrese el nombre del jugador 1: ")
    jugador = buscar_jugador(nom)
    if jugador != None:
        print("Jugador:", jugador["nombre"])
    print()
    nom2 = input("Ingrese el nombre del jugador 2: ")
    jugador2 = buscar_jugador(nom2)
    if jugador2 != None:
        print("Jugador:", jugador2["nombre"])
    print()

#Validador de nombre, creacion y acumulacion de partidas y puntos dentro de un diccionario
    while jugador == None:
        print()
        print("El jugador", nom, "no existe")
        input("Presione ENTER para crear nuevo jugador")
        jugador = {"nombre":nom, "partidas":0, "puntos":0}
        jugadores.append(jugador)
        print("Jugador Creado! Presione ENTER para continuar")
        print()
        print("Hola! ",nom)
        print()
        input("Presione ENTER para continuar")

    while jugador2 == None:
        print()
        print("El jugador",nom2, "no existe")
        input("Presione ENTER para crear nuevo jugador")
        jugador2 = {"nombre":nom2, "partidas":0, "puntos":0}
        jugadores.append(jugador2)
        print("Jugador Creado! Presione ENTER para continuar")
        print()
        print("Hola! ",nom2)
        print()
        print(jugadores)
        input("Presione ENTER para continuar")

    return jugador, jugador2

# Añadir a la función un parámetro del jugador 2.
def turno(turno_jugador_1, jugador1, jugador2): 
    global puntaje1, puntaje2, puntaje_para_ganar
    total_tiro = 0 # Establecer variable en cero
    continuar = True
    while continuar:
        if turno_jugador_1:
            print("Turno de", jugador1["nombre"]) # Mostrar quién está jugando
            tirada = obtener_puntaje()
            if tirada == 0:
                total_tiro = 0
            else:
                total_tiro += tirada
            puntaje1 += total_tiro # Ir actualizando en cada turno el puntaje.
            print("Puntaje de", jugador1["nombre"], ":", puntaje1)
        else:
            print("Turno de", jugador2["nombre"])
            tirada = obtener_puntaje()
            if tirada == 0:
                total_tiro = 0
            else:
                total_tiro += tirada
            puntaje2 += total_tiro # Ir actualizando el puntaje en la partida
            print("Puntaje de", jugador2["nombre"], ":", puntaje2)

        # En caso que haya ganado alguien
        if puntaje1 >= puntaje_para_ganar or puntaje2 >= puntaje_para_ganar: 
            continuar = False
            if turno_jugador_1:
                print("HA GANADO", jugador1["nombre"])
                jugador1["puntos"] += puntaje1 # Actualizar el puntaje y añadirlo a la lista para luego poder comparar quién tiene más
            else:
                print("HA GANADO", jugador2["nombre"])
                jugador2["puntos"] += puntaje2 # Actualizar el puntaje y añadirlo a la lista para luego poder comparar quién tiene más
            input("Presione ENTER para salir")
        elif total_tiro == 0:
            turno_jugador_1 = not turno_jugador_1
        else:
            resp = str.upper(input("Desea seguir tirando? (S/N)"))
            if resp == "N":
                turno_jugador_1 = not turno_jugador_1
    return puntaje1, puntaje2

#Obtener puntajes de los 3 dados con diferentes combinaciones
def obtener_puntaje():
    dados = tirar_dados()
    if dados[0] == dados[1] == dados[2]:
        return 1000
    elif dados[0] == dados[1] or dados[1] == dados[2] or dados[0] == dados[2]:
        return 500
    elif dados[0] == 1 and dados[1] == 6 or dados[0] == 6 and dados[1] == 1 or dados[1] == 1 and dados[2] == 6 or dados[1] == 6 and dados[2] == 1 or dados[0] == 1 and dados[2] == 6 or dados[1] == 6 and dados[2] == 1:
        return 100
    elif dados[0] == 1 or dados[1] == 1 or dados[2] == 1 or dados[0] == 6 or dados[1] == 6 or dados[2] == 6:
        return 50
    else:
        return 0

#Funcion random de los numeros que saldran entre 1 y 6 para los dados
def tirar_dados():
    dados = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    print("dado 1:",dados[0])
    print("dado 2:",dados[1])
    print("dado 3:",dados[2])
    return dados

# Crear variable para jugador con más puntos
def maximo_puntaje():
    max_puntaje = 0
    jugador_Top = None 
    for jugador in jugadores:
        if jugador["puntos"] > max_puntaje: # Buscar el jugador que tiene más puntos haciendo comparativas
            max_puntaje = jugador["puntos"] # Faltaba imprimir algo aquí
            jugador_Top = jugador # Actualizar la variable para que asociar la mayor cantidad de puntos de un jugador a la variable ya creada.

    # Verificar primero que haya algún puntaje
    if jugador_Top:
        print(f"El jugador con más puntos de todos los tiempos es: {jugador_Top}")
    else: 
        print("No se registran puntajes. Juegue una partida para registrar puntajes.")
    
    # Dar una pausa
    input("ENTER para volver al menú anterior")
    return max_puntaje

def nueva_partida():
    global puntaje1, puntaje2
    system("cls")
    print("BIENVENIDOS!")
    input("Presione ENTER para comenzar")
    jugador1, jugador2 = nuevo_jugador() # Llamar a la función de añadir nuevo jugador
    print("EL PUNTAJE PARA GANAR ES:", puntaje_para_ganar)
    input("Presione Enter para tirar los dados")
    print("Comenzó la partida:")
    turno_jugador_1 = True
    puntaje1, puntaje2 = 0, 0  # Reiniciar los puntajes antes de la partida
    turno(turno_jugador_1, jugador1, jugador2) # Iniciar la partida
    
    # Incrementar las partidas jugadas por jugador, y guardarlos para mostrarlos despues
    jugador1["partidas"] += 1 # Actualizar en lista
    jugador2["partidas"] += 1 # Actualizar en lista
    print(f"{jugador1['nombre']} ahora tiene {jugador1['puntos']} puntos en {jugador1['partidas']} partidas.")
    print(f"{jugador2['nombre']} ahora tiene {jugador2['puntos']} puntos en {jugador2['partidas']} partidas.")
    input("Presione ENTER para continuar.")

#Funcion de listar jugadores creados en el juego
def listar_jugadores():
    system("cls")
    print("Lista de jugadores:")
    # Comprobar que haya algo en la lista primero.
    if len(jugadores) == 0:
        print("No hay jugadores creados")
    else: # Recorrer e imprimir el contenido de la lista
        for jugador in jugadores:
            print(f"Nombre: {jugador['nombre']}, Partidas: {jugador['partidas']}, Puntos: {jugador['puntos']}")
    input("ENTER para volver al menú") 

#Funcion para cambiar el puntaje final del juego, para alargarlo o acortarlo    
def cambiar_puntaje_para_ganar():
    global puntaje_para_ganar
    puntaje_nuevo = int(input("Ingrese el nuevo puntaje para ganar partidas: "))
    puntaje_para_ganar = puntaje_nuevo
    print("El puntaje para ganar partidas se ha actualizado a:", puntaje_nuevo) # Mostrar el puntaje nuevo
    input("ENTER para continuar") 

def guardar_partida():
    global partida_guardada
    partida_guardada = True
    print("Partida guardada exitosamente.")
#Funcion para guardar y salir del juego
def salir_del_juego():
    if partida_guardada:
        print("Saliendo del juego...")
    else:
        print("Debes guardar la partida antes de salir.")

opcion = ""
while opcion != "5":
    mostrar_menu()
    opcion = pedir_opcion()
    if opcion == "1":
        nueva_partida()
    elif opcion == "2":
        listar_jugadores()
    elif opcion == "3":
        maximo_puntaje()
    elif opcion == "4":
        cambiar_puntaje_para_ganar()
    elif opcion == "5":
        guardar_partida()
        salir_del_juego()