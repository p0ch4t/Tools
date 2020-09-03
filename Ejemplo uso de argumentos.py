
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from random import choice
import time
import sys


def admin(web,users,passw):														
	url = web		#>>>>   PAGINA WEB DEL FORMULARIO
	post_fields = {'userName': users, "pass": passw, 'isLandpage': "true", 'uuid': "cf0dff3b-274c-4d4e-8276-4d4d283d6a65", 'IDContexto': "null"} 				#>>>>   ESTO ES IMPORTANTE MODIFICARLOS CON LOS CAMPOS DEL FORMULARIO QUE QUIERAN MANDAR, EJ: EN VEZ DE 'pass' cambiar a 'password'
	request = Request(url, urlencode(post_fields).encode())
	urlopen(request)
	print("Se envió el siguiente formulario correctamente:")
	print("")
	print(f"Usuario: {users}")
	print(f"Contraseña: {passw}")
	print("")
	time.sleep(45)										#>>>>>           ESTABLEZCA EL TIEMPO
		
archivo = open("pass.txt", "r")									#En este caso, pass.txt es la wordlist de contraseñas
contraseñas = archivo.read().splitlines()

archivo2 = open("user.txt", "r")								#Y user.txt de los usuarios
usuarios = archivo2.read().splitlines()

for x in usuarios:
	admin(sys.argv[1],x,choice(contraseñas))
