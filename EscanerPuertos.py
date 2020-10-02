import socket

ip = input("Introduzca la IP: ")
port = int(input("Introduzca el Puerto: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resultados = s.connect_ex((ip,port))

if resultados == 0:
	print(f"El puerto {port} se encuentra abierto")
else:
	print(f"El puerto {port} se encuentra cerrado")
