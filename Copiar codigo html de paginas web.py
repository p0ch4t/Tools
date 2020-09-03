"""
requests es una libreria que permite hacer conex http y https (como un navegador)
"""
#Script para copiar codigo html de una pagina

import requests # Hace conexiones http/s (como un navegador Web)

pagina = "pedidosya.com.ar"

url = f"https://{pagina}"
print("Copiando codigo HTML de:",url)
respuesta = requests.get(url)
html = str(respuesta.content) #Copiamos el contenido html
archivo = open(f"{pagina}.html", "w") #Creamos un documento
archivo.write(html) #Escribimos lo que hay en la variable "html"
print(" ")
print("Hecho!")


