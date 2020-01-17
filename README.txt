Nombre de integrantes:
	Daniel Pumarino

Roll:
	201873608-2

Requerimientos:
	Python 3.6 o superior
	Pygames

(recomendacion en Pycharm)

Instrucciones de construccion:
	Construido con la libreria pygame Pygame,
	En el archivo sprites.py se encuentra el objeto originaltank, en el que se guarda los datos originales de cada tanque
		objeto player, que hereda de hereda de pygame.sprite.Sprite y de originaltank, con este objeto se generan los tanques
			y tiene funciones update para poder moverse usando botones y poder crear objetos bala.
		objeto Bullet, obtiene coordenadas de tanque y angulo de posicion, tiene funcion update que hace que el sprite avanze
		objeto Wall, cada muro en el mapa es un muro generado al leer el archivo de mapa
		objeto target, objetos que aparecen en modo 1 jugador,obtenidos de el archivo mapa, son destruidos por disparos
	Archivo settings,
		Setting del juego, como tamaño de la pantalla, frames del juego, e imagenes de objetos
	main.py
		se importan archivos necesarios, se inicializa pygames, una vez inicializado el programa se entra en un loop de la funcion menu1()
		en la cual cada boton presionado guarda informacion que luego sera pasada a la funcion load_data(), en caso de que se presione esc,
		la funcion se llama a si misma para volver a la pantalla principal
		load_data() obtiene informacion para saber que mapa, y que objetos del mapa deben cargarse
		luego de esto, el resto del archivo son condiciones de para ganar, que varian entre 1 y 2 jugadores, en el caso de item, que estos	
		aparezcan.

Ejecucion:
	Ejecutar main.py
	es necesario que este en la misma carpeta: 
		mapa1.txt, mapa2.txt, mapa3.txt
		carpeta: img, snd
		settings.py, sprites.py

Link de video:
	https://youtu.be/lvWfgYS5sjY

Link de Git:
	https://github.com/Daraccel/Tank
	