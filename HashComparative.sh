#!/bin/bash

#Variables definitivas

declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"
check='1'
respuesta='N'

#Funciones

function diccionario(){
	read -p 'Indique su diccionario (EXAMPLE: /usr/share/wordlists/rockyou.txt): ' dic
	x=$(wc -l $dic 2>/dev/null)
	error=$(echo $?)
	}

function Pregunta(){
	x=$(wc -l hashes.txt 2>/dev/null)
	error=$(echo $?)
	if [ $error == '0' ]; then
		read -p "[!] Se encontro un archivo 'hashes.txt' de su ultima visita. Desea continuarlo? [Y/n]: " respuesta
	fi
}

function Conversion1(){
	for i in $(cat $dic); do
		echo $i | md5sum | sed 's/  -//g' >> hashes.txt
		n=$(wc -l hashes.txt | sed 's/ hashes.txt//')
		echo -e "${blueColour}[+] ${endColour}Palabra n°$n: ${yellowColour}'$i'${endColour} convertida!"
		check='0'
	done
}

function Conversion2(){
	for i in $(cat $dic); do
		h=$(echo $i | md5sum | sed 's/  -//g')
		if [[ $(cat hashes.txt) =~ (^|[[:space:]])$h($|[[:space:]]) ]]; then
			echo -e "${redColour}[!] ${endColour}El hash $h ya se encuentra en la lista. No se hicieron modificaciones."
			continue
		fi
		echo $h >> hashes.txt
		n=$(wc -l hashes.txt | sed 's/ hashes.txt//')
		echo -e "${blueColour}[+] ${endColour}Palabra n°$n: ${yellowColour}'$i'${endColour} convertida!"
		check='0'
	done
}


trap ctrl_c INT

function ctrl_c (){
	echo -e "${redColour}\n\n[!] ¡Cerrando el programa..!${endColour}\n"
	wait
       	if [ $check -eq '0' ]; then
        	echo -e "${blueColour}[*] Guardando cambios... ${endColour}\n"
		sleep 2
		echo -e "${blueColour}[*] ${endColour}Se guardaron las ${yellowColour}palabras${endColour} convertidas en el archivo ${turquoiseColour}hashes.txt${endColour}\n"
	fi
	exit 0
}

echo -e "${blueColour}|-------------------------------------------------------------------|${endColour}"
echo -e "${blueColour}|${endColour}                  BIENVENIDO A NUESTRO PROGRAMA                    ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}                                                                   ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}         Con este programa podrás crear una rainbow table          ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}              a base de un diccionario y encontrar                 ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}                   la contraseña de tu hash                        ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}                ${blueColour}[+]${endColour} Autor: Joaquin Pochat                          ${blueColour}|${endColour}"
echo -e "${blueColour}|${endColour}                                                                   ${blueColour}|${endColour}"
echo -e "${blueColour}|-------------------------------------------------------------------|${endColour}"
echo ""

read -p 'Indique su diccionario (EXAMPLE: /usr/share/wordlists/rockyou.txt): ' dic
x=$(wc -l $dic 2>/dev/null)
error=$(echo $?)

while [ $error != 0 ]; do
	echo -e "${redColour}[!] ${endColour}No encontramos ese diccionario, por favor, vuelva a intentarlo: \n"
	diccionario
done

echo ""

Pregunta

echo -e "${blueColour}[+] ${endColour}Leyendo las ${yellowColour}palabras${endColour} del diccionario (este proceso puede tardar alrededor de 1 minuto...)\n"

while [ $respuesta != 'Y' ] && [ $respuesta != 'y' ] && [ $respuesta != 'N' ] && [ $respuesta != 'n' ]; do
	echo -e "${redColour}[!] ${endColour}Por favor ingrese una respuesta valida!"
	Pregunta
done

if [ $respuesta == 'N' ] || [ $respuesta == 'n' ]; then
	Conversion1
fi

if [ $respuesta == 'Y' ] || [ $respuesta == 'y' ]; then
	Conversion2
fi


echo ""
read -p 'Introduzca el hash: ' hash

echo ""
echo -e "${turquoiseColour}[...] ${endColour}Buscando...\n"

for i in $(cat hashes.txt); do

        if [ $i == $hash ]; then
                numhash=$(cat hashes.txt | grep -n $hash | cut -d ":" -f1)
                password=$(cat -n $dic | sed 's/ //g' | grep ^$numhash | awk '{print $2}' | head -n1)
                echo -e "${greenColour}[*] Se ha encontrado su contraseña!\n ${endColour}"
                echo -e "${greenColour}[*] ${endColour}Password: ${yellowColour}$password${endColour}"
                echo ""
                exit 0
        fi


done

echo -e "${redColour}[*] ${endColour}No se encontró el hash :(\n"
