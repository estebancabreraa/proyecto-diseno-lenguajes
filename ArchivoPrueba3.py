#Scanner created with ArchivoPrueba3.ATG data
from AFDFixed.AFD import *


exceptions = ['while','do','if','switch', 'IF', 'WHILE', 'While', 'for', 'FOR', 'For']
adfArray = []
identificador= 'identificador'
temp = AFD(identificador)
tempidentificadorAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidentificadorAcceptance)
tempidentificadorTransitions = {0: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 1: {1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}, {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempidentificadorTransitions)
adfArray.append(temp)
numero= 'numero'
temp = AFD(numero)
tempnumeroAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumeroAcceptance)
tempnumeroTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumeroTransitions)
adfArray.append(temp)
numeroDecimal= 'numeroDecimal'
temp = AFD(numeroDecimal)
tempnumeroDecimalAcceptance = {0: False, 1: False, 2: False, 3: True}

temp.setDictAcceptance(tempnumeroDecimalAcceptance)
tempnumeroDecimalTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}, 2: {46}}, 2: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 3: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumeroDecimalTransitions)
adfArray.append(temp)
numeroHex= 'numeroHex'
temp = AFD(numeroHex)
tempnumeroHexAcceptance = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: True, 7: False, 8: False}

temp.setDictAcceptance(tempnumeroHexAcceptance)
tempnumeroHexTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {2: {72}}, 2: {3: {41}}, 3: {4: ['x']}, 4: {5: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}, 6: {72}}, 5: {7: {72}}, 6: {}, 7: {8: {41}}, 8: {4: ['x']}}

temp.setTransition(tempnumeroHexTransitions)
adfArray.append(temp)
espacioEnBlanco= 'espacioEnBlanco'
temp = AFD(espacioEnBlanco)
tempespacioEnBlancoAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempespacioEnBlancoAcceptance)
tempespacioEnBlancoTransitions = {0: {1: [{9, ' '}]}, 1: {1: [{9, ' '}]}}

temp.setTransition(tempespacioEnBlancoTransitions)
adfArray.append(temp)
cadena= 'cadena'
temp = AFD(cadena)
tempcadenaAcceptance = {0: False, 1: False, 2: False, 3: True}

temp.setDictAcceptance(tempcadenaAcceptance)
tempcadenaTransitions = {0: {1: [{34}]}, 1: {2: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}]}, 2: {3: [{34}]}, 3: {}}

temp.setTransition(tempcadenaTransitions)
adfArray.append(temp)
temp = ''
name = ""
previousName = ''
previousAcceptance = ''
found = False
tokensFound = []
f = open(".txt", "r")
text = f.read()
for i in text:
    temp = temp + i
    for j in range (0,len(adfArray)):
        found, acceptance, name= adfArray[j].simulation(temp)
        if found:
            previousName = name
            previousAcceptance = acceptance
            break
        else:
            if not(j == len(adfArray)-1):
                pass
            else:
                temp = temp[:len(temp)-1]
                if not(previousName == '') and not(previousAcceptance == ''):
                    tokensFound.append((temp,previousName))
                previousName = ''
                temp = i
                for k in adfArray:
                    found, acceptance, name= k.simulation(temp)
                    if found:
                        previousName = name
                        previousAcceptance = acceptance
                        break
                if found:
                    break
if acceptance:
    tokensFound.append((temp,name))
for i in range(0, len(tokensFound)):
    temp = list(tokensFound[i])
    if temp[0] in exceptions:
        index = exceptions.index(temp[0])
        temp[0] = exceptions[index]
        temp[1] = exceptions[index]
        tokensFound[i] = temp
for i in tokensFound:
    print(i)
#print(tokensFound)