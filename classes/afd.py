from classes.afn import *
from classes.leaf import *
from classes.char_validation import char_validator_leaf

def buildAFD(expresion): 

    alphabet = [] 
    for i in expresion:
        if char_validator_leaf(i):
            if not i in ["#","ε"]:
                if not i in alphabet:
                    alphabet.append(i)

    tree = []
    auxiliarTree = []
    cont = 1
    for i in expresion:

        if char_validator_leaf(i):
            if not i == "ε":
                temp = leaf(i,cont)
                tree.append(temp)
                auxiliarTree.append(temp)
                cont = cont + 1
            else:
                temp = leaf(i)
                tree.append(temp)
                auxiliarTree.append(temp)
        else:
            if i == "_":
                second = tree.pop()
                first = tree.pop()
                temp = leaf(i,c1=first,c2=second)
                temp.setAnulable(True if (first.getAnulable() and second.getAnulable()) else False)

                if first.getAnulable():
                    primera = sorted(first.getPrimeraPos())
                    primera = sorted(primera + second.getPrimeraPos())
                    temp.setPrimeraPos(primera)
                else:
                    temp.setPrimeraPos(first.getPrimeraPos())

                if second.getAnulable():
                    ultima = sorted(second.getUltimaPos())
                    ultima = sorted(ultima + first.getUltimaPos())
                    temp.setUltimaPos(ultima)
                else:
                    temp.setUltimaPos(second.getUltimaPos())
                tree.append(temp)
                auxiliarTree.append(temp)
            if i == "|":
                second = tree.pop()
                first = tree.pop()
                temp = leaf(i,first,second)
                temp.setAnulable(True if (first.getAnulable() or second.getAnulable()) else False)
                primera = first.getPrimeraPos()
                for i in second.getPrimeraPos():
                        primera.append(i)
                temp.setPrimeraPos(primera)
                primera = first.getUltimaPos()
                for i in second.getUltimaPos():
                    primera.append(i)
                temp.setUltimaPos(primera)
                tree.append(temp)
                auxiliarTree.append(temp)
            if i == "*":
                temp = leaf(i)
                first = tree.pop()
                temp.setAnulable(True)
                temp.setPrimeraPos(first.getPrimeraPos())
                temp.setUltimaPos(first.getUltimaPos())
                tree.append(temp)
                auxiliarTree.append(temp)

    cont = cont
    siguientepos = {}
    for i in range(1,cont):
        siguientepos.update({i:[]})

    for i in auxiliarTree:
        if i.getLabel() == "*":
            for j in i.getUltimaPos():

                values = siguientepos[j]
                values = values+i.getPrimeraPos()
                values = sorted(values)
                siguientepos.update({j:values})
        if i.getLabel() == "_":
            index = auxiliarTree.index(i)
            c1 = i.getC1()
            c2 = i.getC2()

            for j in c1.getUltimaPos():
                values = siguientepos[j]
                values = values + c2.getPrimeraPos()
                values = sorted(values)
                siguientepos.update({j:values})


    Dstates = []
    labelsDstates = []
    Dstates.append(auxiliarTree[len(auxiliarTree)-1].getPrimeraPos())

    for i in Dstates:
        for l in alphabet: 
            correctLabel = [] 
            for j in i:
                for k in auxiliarTree:                
                    if k.getType() == "c":
                        if k.getPos() == j and k.getLabel() == l:
                            correctLabel.append(j)

            if len(correctLabel) > 0:
                values = []
                for j in correctLabel:
                    values = values + siguientepos[j]
                    values = sorted(list(dict.fromkeys(values)))
                if not values in Dstates:
                    Dstates.append(sorted(values))
                    labelsDstates.append((Dstates.index(i),l,Dstates.index(values)))
                else:
                    labelsDstates.append((Dstates.index(i),l,Dstates.index(values)))

    acceptance = []
    for i in Dstates:

        if cont-1 in i:
            acceptance.append(True)
        else:
            acceptance.append(False)
    return labelsDstates, acceptance