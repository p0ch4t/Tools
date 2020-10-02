##Como filtrar la salida de un output (OPCION2)

import re

texto = '''ASDSADSADASDA<pre>root:/bin/bash
etc:/bin/sh
user:/caca

asdsadsadas

'''

#Borrar lo que viene antes de un string:

salida = re.sub(r'^.*?<pre>', '', texto)						#Con expresiones regulares indican que lo que viene antes de '<pre>' se borre
#print(salida)

#Borrar lo que viene despues de un string:

head, sep, tail = salida.partition('asdsadsadas')				#Se parametriza un separador como con cut -d '' y head sería -f1
#print(head)
