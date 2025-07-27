from colorama import init, Fore, Back, Style
from playsound import playsound
import winsound
import sys
if sys.platform == "win32":
	try:
		import ctypes
		kernel32 = ctypes.WinDLL('kernel32')
		user32 = ctypes.WinDLL('user32')
		hWnd = kernel32.GetConsoleWindow()
		SW_MAXIME = 10
		user32.ShowWindow(hWnd, SW_MAXIME)
	except Exception as e:
		print("Nose pudo agrandar la pantalla")
init(autoreset = True)
#TExto de Bienvenid

def opcion():
    print()
    print(Back.GREEN + "1. Juego Suma")
    print(Back.RED + "2. Juego Resta")

def menu_principal(jugador=None):
	print()
	print("Bienvenid@ a Aventuras Matematicas")
	try:
		winsound.PlaySound('Bienvenido.wav', winsound.SND_FILENAME)
	except Exception as e:
		print("Error al reproducir audio")
		print()
	if jugador is None:
		jugador = input("\nDime tu nombre: ")

	while True:
		print(Back.MAGENTA + f"\nSe Bienvenido {jugador} preparate para jugar") 
		print(Back.CYAN + "Elige un modo de juego")
		opcion()
		op = input("Elige la opcion del Menu con 1 o 2: ")
		if op == '1':
			import mode_suma
			mode_suma.jugar(jugador)
			break
		if op == '2':
			import mode_resta
			mode_resta.jugar(jugador)
			break
		else:
			print(Back.RED + "Error de entrada elige solo 1 o 2")
			print(Back.RED + "Intenta Nuevamente")

if __name__ == "__main__":
    print()
    menu_principal()