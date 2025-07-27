from colorama import init, Fore, Style, Back
import random
from playsound import playsound
import random
import winsound
#iniciar dependencia colorama:
init(autoreset = True)
#el juego:

def jugar(jugador):
	print()
	print(f"\nFantastico, {jugador}, has seleccionado jugar y aprender..")
	print(Fore.GREEN + Style.BRIGHT + """

☼   ^___^
 （„u w u„)
 _U__U__________
|                |
⌗ *
▄▀▀ █░█ █▄░▄█ ▄▀▄
░▀▄ █░█ █░█░█ █▀█
▀▀░ ▀▀▀ ▀░░░▀ ▀░▀* 。*°°
|________________|

""")
	try:
		winsound.PlaySound('Fantastic_s.wav', winsound.SND_FILENAME)
	except Exception as e:
		print("Error al reproducir")
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
  		except ValueError:
  			print(Back.RED + "Error de entrada ingresa un numero entre 1-4")

	vidas = 4
	puntos = 0
	aciertos = 0
	errores = 0
	errores_detalle = []
	operandos = dificultad + 1
	
	while vidas > 0:
		numeros = [random.randint(1, 20) for _ in range(operandos)]
		respuesta_correcta = sum(numeros)
		pregunta = " + ".join(map(str, numeros))
		print(Back.MAGENTA + f"\n¿Cuanto es {pregunta}?")

		try:
			respuesta_usuario = int(input("Tu respuesta: "))
			vidas -=1
		except ValueError:
			print(Back.RED + "¡Ese No es un numero! pierdes una vida >:c")
			winsound.PlaySound('esenoes.wav', winsound.SND_FILENAME)
			vidas -= 1
			errores += 1
			errores_detalle.append({"pregunta": pregunta, "correcto": respuesta_correcta, "respuesta": "No numerico"})
			continue

			
		if respuesta_usuario == respuesta_correcta:
			print(Back.GREEN + "¡Correcto! :3")
			try:
				winsound.PlaySound('correcto.wav', winsound.SND_FILENAME)
			except Exception as e:
				print("Error al reproducir audio")

			puntos += 10
			aciertos += 1
			
			if puntos % 30 == 0:
				vidas += 1
				print(Fore.MAGENTA + Style.BRIGHT + "Has ganado una vida extra!! UwU")
				try:
					winsound.PlaySound('vida_extra.wav', winsound.SND_FILENAME)
				except Exception as e:
					print("Error al reproducir audio")
					print()

		else:
			print(Back.RED + "¡Incorrecto!, la respuesta era:", Fore.RED + f"{respuesta_correcta}")
			try:
				winsound.PlaySound('incorrecto.wav', winsound.SND_FILENAME)
			except Exception as e:
				print("Error al reproducir audio")
				print()
			vidas -= 1
			errores += 1
			errores_detalle.append({"pregunta": pregunta, "correcto": respuesta_correcta, "respuesta": respuesta_usuario})

		print()
		print(Back.CYAN + "Puntos:", Fore.CYAN + f"{puntos}", Back.GREEN + "vidas:", Fore.GREEN + f"{vidas}")
	
	print()
	print(Back.WHITE + Fore.BLACK +  "¡Juego Terminado!")
	try:
		winsound.PlaySound('terminado.wav', winsound.SND_FILENAME)
	except Exception as e:
		print("Error al reproducir audio")
		print()
		

	print(Back.CYAN + "Puntos Totales:", Fore.CYAN + f"{puntos}")
	print(Back.GREEN + "Aciertos:", Fore.GREEN + f"{aciertos}")
	print(Back.RED + "Errores:", Fore.RED + f"{errores}")

	if errores > 0:
		print(Back.RED + "\nDetalle de errores:")
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
			jugar.menu_principal(jugador)  # Pasa el nombre del jugador directamente
			break
		if respuesta == 'n':
			print("adiós")
			try:
				winsound.PlaySound('adios.wav', winsound.SND_FILENAME)
			except Exception as e:
				print("Error al reproducir audio")
			break
		else:
			print("Por favor, responde con 'y' para sí o 'n' para no.")  