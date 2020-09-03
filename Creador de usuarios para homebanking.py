from random import choice

archivo1 = open('user.txt', 'r')								#Indique su primer archivo
txt = archivo1.read().splitlines()

archivo2 = open("user2.txt", "r")								#Indique su segundo archivo
txt2 = archivo2.read().splitlines()

for rep in range(482):
	for i in txt:
		nuevo = choice(txt)

	for x in txt2:
		nuevo2 = choice(txt2)
	
	nuevo3 = nuevo+nuevo2
	print(nuevo3)
