#Scanner created with ArchivoPrueba1.ATG data
from AFDFixed.AFD import *


exceptions = ['while','do','if','switch']
adfArray = []
id= 'id'
temp = AFD(id)
tempidAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempidAcceptance)
tempidTransitions = {0: {1: [{97, 98, 99, 100, 101, 102, 103, 104, 105}]}, 1: {1: [{97, 98, 99, 100, 101, 102, 103, 104, 105}, {48, 49}]}}

temp.setTransition(tempidTransitions)
adfArray.append(temp)
numero= 'numero'
temp = AFD(numero)
tempnumeroAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumeroAcceptance)
tempnumeroTransitions = {0: {1: [{48, 49}]}, 1: {1: [{48, 49}]}}

temp.setTransition(tempnumeroTransitions)
adfArray.append(temp)
temp = ''
name = ""
previousName = ''
previousAcceptance = ''
found = False
tokensFound = []
#text = 'ho(la  10 123dsa2 sad as ads32 93r 2( sa0d ] &  + s  +  ==1 1 ?823?'
f = open("tareas.txt", "r")
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