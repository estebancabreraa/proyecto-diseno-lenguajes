#Nota para el programador repr() returns a printable representation of the given object.

def read_file(file):
    characters = []     #Array para guardar todas líneas debajo del encabezado CHARACTERS
    keywords = []   #Array para guardar todas líneas debajo del encabezado KEYWORDS
    tokens = []     #Array para guardar todas líneas debajo del encabezado TOKENS
    nameATG = ""    #Nombre del compiler
    
    flag = 0    #Bandera para identificar debajo de cual encabezado se encuentra la línea que se esta leyendo

    text_file = open(file, 'r')     #Se abre el documento
    for line in text_file.readlines():  #Se analiza documento linea por linea
        if line[:9] == "COMPILER ":     #Primera linea del compiler, se toma su nombre
            nameATG = line[9:].strip()
        else:
            """
            line == chr(10), representa un line feed
            line[4:] in nameATG, representa el Final del COMPILER
            """
            if (not(line == chr(10)) and not(line[4:] == nameATG)):
                lineStripped = line.strip()
                
                if line.strip() in ["CHARACTERS","KEYWORDS","TOKENS"]:  #Si la linea es un encabezado se cambia el valor de flag
                    if lineStripped == "CHARACTERS":
                        flag = 1
                    elif lineStripped == "KEYWORDS":
                        flag = 2
                    elif lineStripped == "TOKENS":
                        flag = 3
                else:
                    if flag == 1:
                        characters.append(lineStripped)
                    if flag == 2:
                        keywords.append(lineStripped)
                    if flag == 3:
                        tokens.append(lineStripped)
    text_file.close()
    return characters, keywords, tokens, nameATG 