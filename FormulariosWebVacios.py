import time
import requests # Hace conexiones http/s (como un navegador Web)

while 1 == 1:
	url = "https://aurangabadpackersandmovers.in/storage/itau/login.php"
	requests.get(url)
	print("Formulario enviado a https://aurangabadpackersandmovers.in/storage/itau/login.php")
	print("")
	time.sleep(0.1)
	url2 = "https://www.lendabiz.com/js/itau/login.php"
	requests.get(url2)
	print("Formulario enviado a https://www.lendabiz.com/js/itau/login.php")
	print("")
	time.sleep(0.1)
