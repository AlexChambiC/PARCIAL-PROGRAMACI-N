import os, msvcrt, sys

tecla_repetir = b's'
while tecla_repetir==b's' or tecla_repetir==b'S':
	os.system ('cls')
	print ('!Hola mundo!')
	print ()
	sys.stdout.write ('Ingrese numero ')
	tecla_repetir = b'\0'
	while tecla_repetir!=b'1':
		tecla_repetir = msvcrt.getch ()
        