#/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print(f"[X] Ejecute el programa de esta manera: python3 {sys.argv[0]} request.txt")
    sys.exit(1)
else:
    archivo = open(sys.argv[1], 'r')
    request = archivo.read()
    archivo.close()

    headers = request.split("\n\n")[0].split("\n")
    data = request.split("\n\n")[1]
    parameters = []
    parametersKey = {}
    parametersValue = {}

    method = headers[0].split(" ")[0]

    for i in range(len(headers)):
        if (i == 0):
            headerKey = headers[i].split(" ")[1]
            uri = headerKey
        else:
            headerKey = headers[i].split(":")[0]
            if headerKey == "Host":
                host = 'http://'+headers[i].split(": ")[1]
            
    if method == "POST":
        parameters = data.split("&")
    elif method == "GET":
        parameters = uri.split("?")[1].split("&")
    for i in range(len(parameters)):
        parametersKey[i] = parameters[i].split("=")[0]
        parametersValue[i] = parameters[i].split("=")[1]
    
    form = ""
    form += "<html>\n"
    form += "\t<body>\n"
    form += "\t\t<form method=\"" + method + "\" action=\"" + host + uri + "\">\n"
    for i in range(len(parameters)):
        form += "\t\t\t<input type=\"hidden\" name=\"" + parametersKey[i] + "\" value=\"" + parametersValue[i] + "\"/>\n"      
    form += "\t\t\t<input type=\"submit\" value=\"Submit\">\n"
    form += "\t\t</form>\n"
    form += "\t</body>\n"
    form += "<html>\n"

    print(form)