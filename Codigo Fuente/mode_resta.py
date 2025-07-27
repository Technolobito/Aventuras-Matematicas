from colorama import init, Fore, Style, Back #Biblioteca de Texto a color
from playsound import playsound
import random
import winsound

#iniciar pygame



#iniciar dependencia colorama:
init(autoreset = True) #Para que de un autoreseteo la biblioteca colorama

#Logica del juego:
def jugar(jugador): #Llamar a la  variale que deposita el nombre de jugador
    print()
    print(Back.WHITE + Fore.BLACK + f"Fantastico, {jugador}, has seleccionado jugar y aprender..")
    print(Fore.RED + Style.BRIGHT + """
*   ^___^
 （„u w u„)
 _u_u_____________
| *               |
█▀▀▄ █▀ ▄▀▀ ▀█▀ ▄▀▄
█▐█▀ █▀ ░▀▄ ░█░ █▀█
▀░▀▀ ▀▀ ▀▀░ ░▀░ ▀░▀* ° *
|_________________|
""")
    try:
    	winsound.PlaySound('Fantastic_r.wav', winsound.SND_FILENAME)
    except Exception as e:
    	print("Error no se pudo reproducir el sonido", e)
    	print()
    print(Fore.RED + "Buena suerte. la necesitarás :3..")
    print(Fore.RED + f"Por favor, {jugador}, elige sabiamente el número de la dificultad del juego")
    print()
    print(Fore.GREEN + "1. Facil      (2 operandos)")
    print(Fore.YELLOW + "2. Intermedio (3 operandos)")
    print(Fore.RED + "3. Dificil    (4 operandos)")
    print(Fore.MAGENTA + "4. Experto    (5 operandos)")

    while True:
        try:
            dificultad = int(input("Elige la dificultad (1-4): "))
            if dificultad in [1, 2, 3, 4]:
                break
            else:
                print(Back.RED + "Error debes eligir un numero dentro de 1 a 4")
        except ValueError: #por si el jugador no pone nada
            print(Back.RED + "Error de entra ingresa un numero entre 1-4")

    vidas = 4
    puntos = 0
    aciertos = 0
    errores = 0
    errores_detalle = [] #Este es un diccionario  que dira al usuario un deatalle sobre los errores que tubo
    respuesta_correcta = 0
    operandos = dificultad + 1

    while vidas > 0:
        numeros = [random.randint(1, 20) for _ in range(operandos)] #variable de depositar numeros aleatorios en un rango de operandos
        respuesta_correcta = numeros[0]
        for num in numeros[1:]:
            respuesta_correcta -= num
        pregunta = " - ".join(map(str, numeros)) #mostar mensaje de del ejercicios
        print(Back.MAGENTA + f"\n¿Cuanto es {pregunta}?")

        try:
            respuesta_usuario = int(input("Tu respuesta: ")) #pedir la respuesta del jugador
            vidas -=1
        except ValueError: #Esto es por si el usuario no pone un numero entero
            print(Back.RED + "¡Ese No es un numero! pierdes una vida >:c")
            winsound.PlaySound('esenoes.wav', winsound.SND_FILENAME )
            vidas -= 1
            errores += 1
            errores_detalle.append({"pregunta": pregunta, "correcto": respuesta_correcta, "respuesta": "No numerico"})
            continue

        if respuesta_usuario == respuesta_correcta:
        	print(Back.GREEN + "¡Correcto! :3")
        	try:
        		winsound.PlaySound('correcto.wav', winsound.SND_FILENAME)
        	except Exception as e:
        		print("Error no se pudo reproducir el sonido", e)
        	puntos += 10 
        	aciertos += 1
        	if puntos % 30 == 0:
        		vidas += 1
        		print(Back.MAGENTA + "Has ganado una vida extra!! UwU")
        		try:
        			winsound.PlaySound('vida_extra.wav', winsound.SND_FILENAME)
        		except Exception as e:
        			print("Error al reproducir audio")

        else:
            print(Back.RED + "¡Incorrecto!, la respuesta era", Fore.GREEN + f"{respuesta_correcta}")
            try:
            	winsound.PlaySound('incorrecto.wav', winsound.SND_FILENAME)
            except Exception as e:
            	print("Error no se pudo reproducir el sonido", e)
            vidas -= 1
            errores += 1
            errores_detalle.append({"pregunta": pregunta, "correcto": respuesta_correcta, "respuesta": respuesta_usuario})
        print()
        print(Back.CYAN + "Puntos:", Fore.CYAN + f"{puntos}", Back.GREEN + "vidas:", Fore.GREEN + f"{vidas}")

    print(Back.WHITE + Fore.BLACK + "\n¡Juego Terminado!") #Al finalizar el juego mostrara esto
    try:
    	winsound.PlaySound('terminado.wav', winsound.SND_FILENAME)
    except Exception as e:
    	print("Error de audio")
    	print()

    print(Back.CYAN + "Puntos Totales:", Fore.CYAN + f"{puntos}")
    print(Back.GREEN + "Aciertos:", Fore.GREEN + f"{aciertos}")
    print(Back.RED + "Errores:", Fore.RED + f"{errores}")

    if errores > 0:
        print("\nDetalle de errores:")
        for i, error in enumerate(errores_detalle, start = 1):
            print(f"{i}. Pregunta: {error['pregunta']} | correcto: {error['correcto']} | Tu respuesta: {error['respuesta']}")

    while True:
        try:
        	winsound.PlaySound('volverjugar.wav', winsound.SND_FILENAME)
        except Exception as e:
        	print("Error al reproducir audio")
        	print()
        respuesta = input("\n¿Quieres volver a jugar? (y/n): ").strip().lower()
        if respuesta == 'y':
            import jugar
            jugar.menu_principal(jugador)  # Reciclar el nombre del jugador que se puso anteriormente en el script principal
            break
        elif respuesta == 'n':
            print("adiós")
            try:
            	winsound.PlaySound('adios.wav', winsound.SND_FILENAME)
            except Exception as e:
            	print("Error al reproducir audio")
            	print()
            break
        else:
            print("Por favor, responde con 'y' para sí o 'n' para no.")  