"""
requests es una libreria que permite hacer conex http y https (como un navegador)
"""
import requests
import time

lista_sitios = [
"istea.edu.ar",
"educacionit.com",
"istea.azurewebsites.net",
"www.colegiomilitar.mil.ar",
"www.mercadolibre.com.ar",
"www.gba.gob.ar"
]

for sitio in lista_sitios:
	try:
		url = "https://"+sitio
		respuesta = requests.get(url)
		codigo = respuesta.status_code
		server = respuesta.headers['Server']
		timeout = respuesta.headers['Keep-Alive']
		Date = respuesta.headers['Date']

		if codigo == 200:
			print(f"[+] Sitio: { url } ") # nueva forma de imprimir
			print(f"[+] Sever: { server } ")
			print(f"[+] timeout: { timeout } ")
			print(f"[+] Date: { Date } ")
		else:
			print(f"No se encontro la url {url} codigo: { codigo }")
		time.sleep(2)
		print("------------------------------------------")
	except:
		print(f"Hubo un error al acceder a {url}")
