#Scanner created with Double.ATG data
from AFDFixed.AFD import *


exceptions = ['while','do','if','switch']
adfArray = []
number= 'number'
temp = AFD(number)
tempnumberAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempnumberAcceptance)
tempnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempnumberTransitions)
adfArray.append(temp)
decnumber= 'decnumber'
temp = AFD(decnumber)
tempdecnumberAcceptance = {0: False, 1: False, 2: False, 3: True}

temp.setDictAcceptance(tempdecnumberAcceptance)
tempdecnumberTransitions = {0: {1: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 1: {1: {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}, 2: {46}}, 2: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}, 3: {3: [{48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]}}

temp.setTransition(tempdecnumberTransitions)
adfArray.append(temp)
white= 'white'
temp = AFD(white)
tempwhiteAcceptance = {0: False, 1: True}

temp.setDictAcceptance(tempwhiteAcceptance)
tempwhiteTransitions = {0: {1: [{32, 9, 10, 13}]}, 1: {1: [{32, 9, 10, 13}]}}

temp.setTransition(tempwhiteTransitions)
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