##Como filtrar la salida de un output (OPCION1)

import re

texto = '''ASDSADSADASDA<pre>root:/bin/bash
etc:/bin/sh
user:/caca

asdsadsadas

'''

#Borrar lo que viene antes de un string:

tmp1 = texto.split('<pre>', 1)			#Crea una lista dividiendo por '<pre>' con 2 elementos (0 y 1)
tmp2 = tmp1[1]							#Selecciona el elemento '1' de la lista
tmp3 = tmp2.split('asdsadsadas', 1)		#Crea una lista dividiendo por 'asdsadsadas' con 2 elementos (0 y 1)
salida = tmp3[0]						#Selecciona el elemento '0' de la lista
print(salida)
