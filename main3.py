#Metodo para coverir listas en string
def listToString(s):  
    str1 = ""  
    for ele in s:
        str1 += ele
    return str1 

#Definicion para completar listas de letras. 
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def create_word(c1, c2):
    word = ""
    for c in char_range(c1, c2):
        word += c
    word = str(word)
    return word

# definicion para encontrar palabras especificas dentros del archivo 
def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results[0][1]

# definicion para guardar los conjuntos y los keywords
def save_groups(file_name, title, stop):
    f = open(file_name, "r")
    key = False
    i = 0
    elements = []
    for line in f:
        if title in line:
            key = True
        if key == True:
            for e in line:
                if e == '=':
                    elements.append(line)
            if stop in line:
                key = False
    return elements

# Creamos la variable para ANY
AnyWord = ""
for i in range(33, 128):
    if i == 34:
        pass
    elif i == 13:
        pass
    elif i == 10:
        pass
    elif i == 9:
        pass
    else:
        AnyWord += chr(i)
    
# en esta lista guardaremos las instrucciones del porgrama que va a generar el proyecto. 
instrucciones = []
# en esta lista guardaremos las indicaciones que encuentra en el file que tiene que leer. 
indicaciones = []

# aqui empezamos hacer las indicaciones segun lo que lea en los archivos
#  primero lo hacemos para characters  
characters_key = False
u = 0
c1 = ""
c2 = ""
s = 0
less_word = ""
less_number = 0
characters_elementos = save_groups("max.atg", "CHARACTERS", "TOKENS\n")
for posicion in characters_elementos: 
    if "CHR" in posicion:
        posicion = posicion.replace("CHR", "chr")
    if " ANY " in posicion:
        posicion = posicion.replace("ANY", '"'+AnyWord+'"')
    elif "ANY-" in posicion:
        posicion = posicion.replace(" ANY", '"'+AnyWord+'"')
    if ".." in posicion:
        for i in posicion:
            if i == "'":
                u += 1
            if u == 1:
                c1 += i
            if u == 3:
                c2 += i
        c1 = c1.replace("..", "")
        c1 = c1.replace("'", "")
        c2 = c2.replace("..", "")
        c2 = c2.replace("'", "")
        c3 = create_word(str(c1), str(c2))
        posicion = characters_elementos[s].replace("' .. '", c3)
        c1 = ""
        c2 = ""
        u=0
    if "-" in posicion:
        for i in posicion:
            if i == '"':
                less_number += 1
            if less_number == 2:
                less_word += i
            if i == "." and less_number == 2:
                less_word = less_word.replace('"', '')
                posicion = posicion.replace(less_word, "")
        less_word = ""
        less_number = 0
    s += 1
    instrucciones.append(posicion.replace('.', ''))

# seguimos con keywords
keywords_key = False
i = 0
keywords_string = ""
keywords_words = []
keywords_elementos = save_groups("max.atg", "KEYWORDS\n", "TOKENS")
for posicion in keywords_elementos:  
    while i < len(posicion):
        if posicion[i]=="=":
            keywords_key=True
        if keywords_key == True:
            keywords_string += posicion[i]
            if posicion[i] == ".":
                keywords_key=False
        i += 1
    i = 0
    keywords_string = keywords_string.replace("=", "")
    keywords_string = keywords_string.replace(".", "")
    keywords_words.append(keywords_string)
    keywords_string = ""

instrucciones.append("array_keywords = []\n")
u = 1
for i in keywords_words:
    instrucciones.append("keyword%s = %s\n" %(u, i))
    instrucciones.append("array_keywords.append(keyword%s)\n" % u)
    u += 1

# Agregamos otras instrucciones que van a sevir para leer el otro documento a recibir
instrucciones.append('palabra_actual = ""\n')
instrucciones.append('array_elementos = []\n')
instrucciones.append("archivo_recibido = input('Escribe el nombre del archivo a leer (con su extension): ')\n")
instrucciones.append("file = open(archivo_recibido, 'r')\n")
instrucciones.append("for line in file:\n"+"\tfor e in line:\n"+"\t\tif e == '\\n':\n"+"\t\t\te = ' '\n"+"\t\tif e == ' ':\n")
instrucciones.append("\t\t\tarray_elementos.append(palabra_actual)\n"+"\t\t\tpalabra_actual = ''\n"+"\t\t\te = ''\n")
instrucciones.append("\t\tpalabra_actual += e\n")
instrucciones.append("array_elementos.append(palabra_actual)\n")

# seguimos con tokens
tokens_elementos = save_groups("max.atg", "TOKENS", "PRODUCTIONS")
tokens_array = []
for line in tokens_elementos:
    tokens_array.append(line)

w = 0
for line in tokens_elementos:
    if '..' in line:
        tokens_elementos[w] = tokens_elementos[w].replace('..', ',,')
    w += 1

tokens_key = False
tokens_words = []
token_word = ""
for line in tokens_elementos:
    for i in line:
        if i == "=":
            tokens_key = True
            token_word = token_word.replace("\n", "")
            tokens_words.append(token_word)
            token_word = ""
        if tokens_key == False:
            token_word += i
        if i == ".":
            tokens_key = False

tokens_key = False
tokens_instructions = []
token_word = ""
numbers_of_points = 0
for line in tokens_elementos:
    for i in line:
        if i == ".":
            numbers_of_points += 1
        if numbers_of_points > 1:
            line = line.replace(".", ",", 1)
            numbers_of_points = 0
    numbers_of_points = 0
    for i in line:
        if tokens_key == True:
            token_word += i
        if i == ".":
            tokens_key = False
            token_word = token_word.replace("\n", "")
            token_word = token_word.replace(" ", "")
            tokens_instructions.append(token_word)
            token_word = ""
        if i == "=":
            tokens_key = True

# Ahora vamos a agregar instrucciones al documento para evaluar los token ahora que ya los tenemos
# separagos por nombre e intrucciones.       
instrucciones.append("print('Mensaje encontrrado en el documento:'+str(array_elementos))\n")  

#Vamos a dar instrucciones para encontras las keywords
instrucciones.append("u = 0\n"+"new_array_keywords = []\n"+"for line in array_elementos:\n")
instrucciones.append("\tif line in array_keywords:\n"+"\t\tprint('Se encontro keyword: %s' % line)\n")
instrucciones.append("\t\tnew_array_keywords.append(line)\n"+"\t\tarray_elementos.pop(u)\n"+"\tu += 1\n")

# separamos los ORs de tokens
t = 0
isOpen = False
for line in tokens_instructions:
    for i in line:
        if i == "{":
            isOpen = True
        if (isOpen == True) and (i == "|"):
            tokens_instructions[t] = line.replace("|", " or ", 1)
        if i == "}":
            isOpen = False
    t +=1

y = 0
isOpen = False
key_four = False
word_four = ""
array_fourword = []
for line in tokens_instructions:
    for i in line:
        if i == "{":
            isOpen = True
        if (i == ".") or (i == "|"):
            key_four = False
            array_fourword.append(word_four)
            word_four = ""
        if key_four == True:
            word_four += i
        if isOpen == False:
            if i == "|":
                key_four = True
        if i == "}":
            isOpen = False
    y += 1

q = 0
for line in array_fourword:
    if len(line) > 2:
        tokens_instructions.insert(q, line)
        tokens_words.insert(q, str(tokens_words[q-1])+str(q))
    q += 1    
# Aqui comienza el analisis de las instrucciones de los tokens 
# esta en especifico para las que traen etiqueta 
s = 0
for i in tokens_instructions:
    if '"|"' in i:
        tokens_instructions.pop(s+1)
    s += 1

# Aqui vamos a tratar los [] para que sean mas facil leerlos mas adelante
numbers_of_keys = 0
word_five = ""
word_five_array = []
for line in tokens_instructions:
    for i in line:
        if i == "[" or i == "]":
            numbers_of_keys += 1
        if numbers_of_keys == 1:
            word_five += i
        if numbers_of_keys == 2:
            word_five += i
            word_five_array.append(word_five)
            word_five = ""
            numbers_of_keys = 0

s = 0
for line in tokens_instructions:
    for line2 in word_five_array:
        if line2 in line:
            tokens_instructions[s] = tokens_instructions[s].replace(line2, "")
            tokens_instructions.insert(s, line2)
            tokens_words.insert(s, str(tokens_words[s])+str(s))
    s += 1

#Aqui vamos extraer esas palabras que suelen venir entre ""
word_three = ""
array_thirdwords = []
key_three = False
j = 0
for line in tokens_instructions:
    if "(" in line and "|"in line:
        line = line.replace('"|"', " or ", 1)
    for i in line:
        if i == "'" or i == '"':
            j += 1
        if j == 1:
            word_three += i
        if j == 2:
            word_three = word_three.replace('"', '')
            word_three = word_three.replace("'", "")
            array_thirdwords.append(word_three)
            word_three = ""
            j = 0
            if len(array_thirdwords) > 2:
                array_thirdwords.pop(-1)

# Correjimos algunas palabras que pueden dar problemas 
q = 0
work_t = ""
number_comillas = 0
for line in tokens_instructions:
    if "CHR(" in line:
        tokens_instructions[q] = tokens_instructions[q].replace('"CHR("', '"chr("')
    for i in line:
        if i == '"':
            number_comillas += 1  
    if number_comillas >= 4:
        tokens_instructions[q] = tokens_instructions[q].replace('"', '')
    number_comillas = 0
    q += 1

j=0
i = 0
word_one = ""
word_two = ""
plus_key_one = False
joker3 = ""
number_of_parentesis = 0
while i < len(tokens_instructions):
    if "[" in tokens_instructions[i]:
        joker3 = tokens_instructions[i]+"+"
        joker3 = joker3.replace("[", "")
        joker3 = joker3.replace("]", "")
    if "{" in tokens_instructions[i]:
        joker2 = str(tokens_words[i])
        for e in tokens_instructions[i]:
            if plus_key_one == True:
                if e == "}":
                    plus_key_one = False
                    break
                word_two += e
            if e == "{":
                plus_key_one = True
            if plus_key_one == False:
                word_one += e
        if "(" in word_one and ")" not in word_one:
            word_one += ")"
            if 'chr(' in word_one:
                word_one = word_one.replace('chr(','"chr("+')
                word_one = word_one.replace(')','+")"')
        instrucciones.append("key = False\n"+"isToken = False\n"+"number_of_errors = 0\n"+"for line in array_elementos:\n")
        instrucciones.append("\tfor i in line:\n"+"\t\tif key == False:\n"+"\t\t\tif i in "+joker3+word_one+":\n")
        joker3=""
        number_of_parentesis = 0
        instrucciones.append("\t\t\t\tisToken = True\n"+"\t\t\t\tkey = True\n"+"\t\t\telse:\n")
        instrucciones.append("\t\t\t\tisToken = False\n"+"\t\t\t\tnumber_of_errors +=1\n"+"\t\tif key == True:\n")
        if "or" in word_two:
            word_two = word_two.replace("or", "or i in")
        instrucciones.append("\t\t\tif i in "+word_two+":\n"+"\t\t\t\tisToken = True\n")
        instrucciones.append("\t\t\telse:\n"+"\t\t\t\tif isToken == True:\n"+"\t\t\t\t\tnumber_of_errors += 1\n")
        instrucciones.append("\tkey = False\n")
        if '"' in tokens_instructions[i]:
            if "or" in tokens_instructions[j]:
                array_thirdwords[j] = array_thirdwords[j].replace(") or (", ")' in line or '(")
            instrucciones.append("\tif '"+array_thirdwords[j]+"' in line:\n"+"\t\tisToken = True\n")
            instrucciones.append("\t\tnumber_of_errors -= len('"+array_thirdwords[j][:3]+"')\n")
            j += 1
            instrucciones.append("\telse:\n"+"\t\tisToken = False\n")
        if '"digit{digit}.' in joker2:
            joker2 = joker2.replace('"digit{digit}.', '')
        instrucciones.append("\tif isToken == True and number_of_errors <= 0:\n"+"\t\tprint('SE ENCONTRO UN TOKEN TIPO: "+joker2+"')\n")
        instrucciones.append("\tnumber_of_errors = 0\n")
        word_one=""
        word_two=""
    else:
        joker1 = str(tokens_instructions[i])
        joker2 = str(tokens_words[i]) 
        instrucciones.append("for line in array_elementos:\n"+"\tfor i in line:\n")
        instrucciones.append("\t\tif i in "+joker1+":\n"+"\t\t\tprint('SE ENCONTRO UN TOKEN TIPO: "+joker2+"')\n")
        if ".:" in instrucciones[-1]:
            instrucciones[-1] = instrucciones[-1].replace(".:", ":")
    i += 1


#########################################################
# A PARTIR DE AQUI COMIENZA EL PROYECTO # 3             #
#########################################################
instrucciones.append("\n\nimport sys\n")
instrucciones.append("\nleft_right = []\nword = ''\nposition = 0\narray_of_symbols = []")
# Empezamos con PRODUCTIONS
f = open("max.atg", "r")
key = False
productions_elementos = ""
for line in f:
    if "END Max" in line:
        key = False
    if key == True:
        productions_elementos += line
    if "PRODUCTIONS" in line:
        key = True

# primero vamos a recopilar los simbolos para poder reconocerlos 
symbol = ""
symbol_key = False
symbol_key_2 = 0
for i in productions_elementos:
    if i == "}":
        symbol_key = False
    if i == "{":
        symbol_key = True
    if symbol_key == True:
        if i == '"':
            symbol_key_2 += 1
            if symbol_key_2 == 2:
                symbol_key_2 = 0
                symbol = symbol.replace('"', '')
                message = "\narray_of_symbols.append('%s')" %symbol
                instrucciones.append(message)
                symbol = ""
        if symbol_key_2 == 1:
            symbol += i

instrucciones.append("\nfor line in array_elementos:\n\tfor i in line:\n\t\tif i in array_of_symbols:")
instrucciones.append("\n\t\t\tword = word.replace(i, '')\n\t\t\ti = i.replace(i, '')\n\t\t\tleft_right.append(word)\n\t\t\tword = ''\n\t\tword += i\n")
instrucciones.append("\nleft_right.append(word)\nactual=0")
instrucciones.append("\nfor e in array_elementos:\n\tbefore = actual\n\tactual = e")
instrucciones.append("\n\tif actual == before and (actual in array_of_symbols or before in array_of_symbols):\n\t\tprint('Dos simbolos repetidos')\n")

actual_key =""
before_key = ""
flag = before_key+actual_key
bucket = ""
bucket_2 = ""
bucket_3 = ""
bucket_3_1 = ""
bucket_4 = ""
bucket_4_1 = ""
bucket_5 = ""
acomodo = ""
is_open = True
is_real_symbol = True
is_into_while = False
into_function = False
into_function_key = True
into_if = False
into_if_key = True
is_while_instruction = 0
is_function_instruction = 0

instrucciones.append("\ntry:")

for i in productions_elementos:
    before_key = actual_key
    actual_key = i
    flag = before_key+actual_key

    if into_if == True:
        if into_if_key == True:
            bucket_5 += i

    if into_function == True:
        if i=="(" or flag=="(." or i=="{" or i=="|":
            into_function_key = False
        if into_function_key == True:
            bucket_4 = bucket_4.replace(".)", "")
            bucket_4 = bucket_4.replace("\t.", "")
            bucket_4 += i
            if i == ">":
                bucket_4 = bucket_4.replace("\n", "")
                bucket_4 = bucket_4.replace("\t", "")
                bucket_4 = bucket_4.replace("<", "(")
                bucket_4 = bucket_4.replace(">", ")")
                bucket_4 = bucket_4.replace('["-"    ]', '')
                bucket_4_1 = ""
                for e in bucket_4:
                    if e == "(":
                        is_function_instruction += 1
                        e = e.replace("(", "")
                    elif e == ")":
                        is_function_instruction += 1
                        is_function_instruction = 0
                    if is_function_instruction == 1:
                        bucket_4_1 += e
                message = "\n\t\t%s = %s" %(bucket_4_1, bucket_4)
                instrucciones.append(message)
                bucket_4 = ""
        elif i==")" or flag==".)" or i=="}":
            into_function_key = True
        into_function = False

    if is_into_while == True:
        if i == '"' or i == ")" or i =="(" or flag=="(." or flag == ".)":
            is_while_instruction += 1 
            if is_while_instruction > 1:
                is_while_instruction = 0
        if is_while_instruction == 0:
            bucket_3 = bucket_3.replace(")", "")
            bucket_3 = bucket_3.replace('"', '')
            bucket_3 += i
        if i == "|":
            bucket_3 = ""
        if i == ">":
            bucket_3 = bucket_3.replace("(", "")
            bucket_3 = bucket_3.replace("}", "")
            bucket_3 = bucket_3.replace("<", "(")
            bucket_3 = bucket_3.replace(">", ")")
            bucket_3 = bucket_3.replace("\n", "")
            bucket_3 = bucket_3.replace("     ", "")
            bucket_3_1 = ""
            for e in bucket_3:
                if e == "(":
                    is_while_instruction += 1
                    e = e.replace("(", "")
                elif e == ")":
                    is_while_instruction += 1
                if is_while_instruction == 1:
                    bucket_3_1 += e
            message = "\n\t\t\t%s = %s" %(bucket_3_1, bucket_3)
            instrucciones.append(message)
            bucket_3 = ""

    if i == "[":
        into_if = True
    elif i== "]":
        into_if = False
        if len(bucket_5) > 0:
            bucket_5 = bucket_5.replace("(.", "")
            bucket_5 = bucket_5.replace("]", "")
            bucket_5 = bucket_5.replace("\n", "")
            bucket_5 = bucket_5.replace("\t", "")
            acomodo = "\t\t"
            message = "\n\t\tif %s in array_of_symbols:" %bucket_5
            instrucciones.append(message)
            bucket_5 = ""

    if i == "{":
        is_into_while = True
        message = "\n\t\twhile len(left_right) > 0:"
        instrucciones.append(message)
        acomodo = "\t\t"
    if i == "}":
        is_into_while = False
        message = "\n\t\t\tleft_right.pop(0)"
        instrucciones.append(message)
        acomodo = "\t"

    if flag == "(.":
        is_real_symbol = False
        is_open = False
        into_if_key = False
    if flag == ".)":
        is_real_symbol = True
        is_open = True
        into_if_key = True
        bucket_2 = bucket_2.replace(".", "")
        bucket_2 = bucket_2.replace("self", "")
        bucket_2 = bucket_2.replace("sort", ".sort")
        message = "\n\t%s%s" %(acomodo, bucket_2)
        instrucciones.append(message)
        bucket_2 = ""

    if i == "<":
        i = i.replace("<", "(")
    elif i == ">":
        i = i.replace(">", ")")
    
    if is_real_symbol == True:
        if i == "=":
            into_function = True
            if "(" in bucket or ")" in bucket:
                message = "\n\tdef %s:\n\t\tpass" %bucket
                instrucciones.append(message)
                bucket = ""
                acomodo = "\t"
            else:
                message = "\n\tdef %s():\n\t\tpass" %bucket
                instrucciones.append(message)
                bucket = ""
                acomodo = "\t"
    
    if flag == "\t.":
        i = i.replace(".", "")
        bucket = ""
        acomodo = ""
        bucket_4 = ""
        into_function = False

    if is_open == True:
        bucket += i
    if is_open == False:
        bucket_2 += i

    if "\n" in bucket:
        bucket = bucket.replace("\n", "")

instrucciones.append("\nexcept:\n\tprint('Algo ha salido mal :(') \n\tprint('revisa los elementos que has ingresado')")
# Creacion del documento 
g = open("programa_generado.py", "w")
DIB = listToString(instrucciones)
g.write(DIB)
g.close()