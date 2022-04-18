from DirectAFD.AFD import *
from DirectAFD.builder import buildAFD
from AFDFixed.AFD import *  
from PostfixGen.infixtopostfix import *

#Convierte elementos de una lista en un string
def extractExp(expresion):
    newExpresion = ""
    for i in expresion:
        newExpresion = newExpresion + i
    return newExpresion

#Convierte elementos de una lista en un string
def word(expresion):
    newExpresion = ""
    for i in expresion:
        newExpresion = newExpresion + i
    return newExpresion

#Crea lista con los valores ascci 
def asciiValuesList(expresion):
    newExpresion = []
    for i in expresion:
        newExpresion.append(ord(i))
    return newExpresion

#Convierte lista a set
def listToSet(listElements):
    temp = set()
    try:
        for i in listElements:
            temp.add(i)
    except:
        temp.add(listElements)
    return temp

#Función de calcular la diferencia entre dos sets
def subsCharacters(data, charactersDict):
    keys = list(charactersDict.keys())
    values = list(charactersDict.values())
    for i in range (0,len(data)):
        if type(data[i]) == str:
            if not(data[i]=="ANY"):
                data[i] = values[keys.index(data[i])]
            else:
                data[i] = rangeCharacter([[00],[255]])
        elif type(data[i]) == int:
            temp = set()
            temp.add(data[i])
            data[i] = temp
        elif type(data[i]) == list:
            data[i] = listToSet(data[i])
    temp = set()
    count = 0
    for i in data:
        if count == 0:
            count = 1
            try:
                temp.update(i)
            except:
                temp.add(i)
        else:
            second = set(i)
            result = temp - second
            temp = result
    return temp

#Función de calcular la suma entre dos sets
def addCharacters(data, charactersDict):
    keys = list(charactersDict.keys())
    values = list(charactersDict.values())
    for i in range (0,len(data)):
        if type(data[i]) == str:
            data[i] = values[keys.index(data[i])]
        elif type(data[i]) == int:
            temp = set()
            temp.add(data[i])
            data[i] = temp
        elif type(data[i]) == list:
            data[i] = listToSet(data[i])
    temp = set()
    for i in data:
        try:
            temp.update(i)
        except:
            temp.add(i)
    return temp

"""
Calcula los valores ascii entre dos
ejemplo: si tiene 0 en la primera posición y 255 en la segunda. crea un set con todos los valores que estan desde 0 hasta 255 
"""
def rangeCharacter(rangeCharacters):
    begin = rangeCharacters[0] 
    end = rangeCharacters[1] 
    temp = set()
    for i in range(begin[0],end[0]+1):
        temp.add(i)
    return temp

#Leer README
def createCharactersDict(characters):
    charactersDict = {}
    for i in characters:
        index = i.index("=") + 2
        name = i[:index-3]  #Se toma el nombre del character
        info = i[index:]   #Se toma toda la informacion del character
        j = 0
        #Variable que tendra todas las palabras y numeros que vaya encontrando
        output = []
        #Variable para formar las palabras 
        exp = []
        #variables para range
        range = []
        #variables para suma
        addition = []
        add = 0
        #variables para resta
        substraction = []
        subs = 0
        #flag de "
        count = 0
        while j < len(info)-1:  #Se analiza todo la informacion
            if info[j] == '"':
                if count == 0:
                    count = 1
                else:
                    output.append(asciiValuesList(exp))
                    exp = []
                    count = 0
            elif info[j] == "." and count == 0:
                try:
                    range.append(output.pop())
                except:
                    pass
            elif info[j] == "+" and count == 0:
                if not(len(exp)==0): 
                    output.append(word(exp))
                    exp = []
                add = 1
            elif info[j] == "-" and count == 0:
                if not(len(exp)==0): 
                    subs = 1
                    output.append(word(exp))
                    exp = []
            elif info[j] == '(':
                temp = extractExp(exp)
                exp = []
            elif info[j] ==')':
                if temp == "CHR":
                    output.append(int(extractExp(exp)))
                    exp = []
            elif (j == len(info)-2 and info[j].isalpha()):
                if not(len(exp) == 0):
                    exp.append(info[j])
                    output.append(word(exp))
                    exp = []
            else:
                exp.append(info[j])
            j = j + 1
        if add:
            output = addCharacters(output,charactersDict)
        if subs:
            output = subsCharacters(output,charactersDict)
        elif not(len(range) == 0):
            range.append(output.pop())
            output = rangeCharacter(range)
        try:
            new_set = set(output[0])
        except:
            new_set = set(output)
        charactersDict.update({name:new_set})
        
    return charactersDict

#Leer README
def createKeywordsDict(charactersDict, keywords):
    keywordsDict = {}
    for i in keywords:
        index = i.index("=") + 2
        name = i[:index-3]  #Se toma el nombre del character
        info = i[index:].replace('"', '')
        info = info.replace('.', '')
        keywordsDict.update({name:info})
    return keywordsDict

#Leer README
def createTokensDict(charactersDict, tokens, specialCharacters, special):
    specialKeys = list(specialCharacters.keys())
    specialValues = list(special.values())
    keys = list(charactersDict.keys())
    tokensDict = {}
    exceptions = []
    for i in tokens:
        if not ("IGNORE SET ignore" in i):
            index = i.index("=") + 2
            name = i[:index-3]  #Se toma el nombre del character
            info = i[index:].replace('"', '')
            dotOccurrence = info.count('.')
            indexDot = info.find(".")

            if dotOccurrence == 2 and (info[indexDot-1]=='"' and info[indexDot+1]=='"'):
                info = info[:indexDot-1]+""+info[indexDot+2:]

            if "EXCEPT " in info:
                index = info.index("EXCEPT ") + 7
                tempExc = info[index:len(info)-1]
                exceptions.append(tempExc)
                info = info.replace((' EXCEPT '+ tempExc+'.'), '')
            else:
                exceptions.append(None)

            if " " in info:
                info = info.replace(' ', '')

            if "hexdigit" in info:
                index = keys.index("hexdigit")
                info = info.replace('hexdigit',str(index))
            if "stringletter" in info:
                index = keys.index("stringletter")
                info = info.replace('stringletter',str(index))
            
            for j in range (0,len(keys)):
                if keys[j] in info:
                    info = info.replace(keys[j], str(j))

            if '.' in info[len(info)-1]:
                info = info[:len(info)-1]
                for j in range (0, len(specialKeys)):
                    if specialKeys[j] in info:
                        info = info.replace(specialKeys[j], specialValues[j])
                if "[" in info:
                    info = info.replace('[', '(ε|').replace(']', ')')
                info = info.replace('{', '(').replace('}', ')*')
                tokensDict.update({name:info})
            else:
                for j in range (0, len(specialKeys)):
                    if specialKeys[j] in info:
                        info = info.replace(specialKeys[j], specialValues[j])
                if "[" in info:
                    info = info.replace('[', '(ε|').replace(']', ')')
                info = info.replace('{', '(').replace('}', ')*')
                tokensDict.update({name:info})
    return tokensDict,exceptions

#Leer README
def functionsCreator(tokensDict, KeywordsDict):
    tokensArray = []
    for i in list(tokensDict.keys()):
        expresion = convertOperators(tokensDict.get(i))
        nuevaExpresionComputable = computableExpresion(expresion)
        postfixexpNueva = infixaPostfix(nuevaExpresionComputable)+["#","_"]
        labelsDstates, acceptance, acceptanceDict = buildAFD(postfixexpNueva)
        newAFD = AFD(i)
        newAFD.firstConstructor(labelsDstates, acceptanceDict)
        print(labelsDstates)
        print(acceptanceDict)
        tokensArray.append(newAFD)
    return tokensArray