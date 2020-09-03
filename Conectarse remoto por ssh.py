#Netmiko

from netmiko import ConnectHandler
from netmiko import Netmiko

def admin(ip,cmd):
	try: #encerramos el codigo en try except para proteger el codigo
		print("Conectando a :", ip, "Comando:",cmd)#muestro ip a donde nos conectamos
		conex = Netmiko(host=ip,username="root",  password="toor", device_type="linux") # creo una conexion y la guardo en la variable conex 
		conex.find_prompt()# encuentro el promt
		print(conex.send_command(cmd)) # envio de comandos por ssh
		conex.disconnect() # desconecto la sesion ssh 
		print("-----------------------------------------------------------------------")
	except:
		print("No se pudo conectar a:", ip)
		pass

lista_srv_linux = [ "192.168.0.95", "192.168.0.51","192.168.0.47"]
comando = "free -h"

for ip in lista_srv_linux:
	admin(ip,comando)
