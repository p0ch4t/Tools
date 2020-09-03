#Conocer la geo localizacion de una direccion ip

import requests # Hace conexiones http/s (como un navegador Web)
import json # maneja archivos json
import ipaddress

lista_ip = ipaddress.ip_network("200.68.125.0/28")

for ip in lista_ip:
    try:
        url = f"https://ip.seeip.org/geoip/{ip}"
        print("Ingresando a:",url)
        respuesta = requests.get(url)
        archivo_json = json.loads(respuesta.text)#guardamos la respuesta json en una variable para manipularla como un json posta
        print(archivo_json)
    except:
        print("Conexion fallida a", ip)
        pass
