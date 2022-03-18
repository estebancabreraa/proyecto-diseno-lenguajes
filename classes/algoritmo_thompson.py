from classes.afn import *
from classes.char_validation import char_validator_thompson
epsilon = 'ε'


def ThompsonAlgorithm(processed_expresion):
    afn_struct = []
    cont = 1
    
    for i in processed_expresion:
        if (char_validator_thompson(i)):
            afn_struct.append(AFN(cont, cont+1,i))
            cont = cont + 2

        if i == "|":
            temp_afn = AFN(cont, cont + 1, epsilon)
            item2 = afn_struct.pop()
            item1 = afn_struct.pop()
            temp_afn.unionOperator(item1,item2)
            afn_struct.append(temp_afn)
            cont = cont + 2

        if i == "_":
            item2 = afn_struct.pop()
            item1 = afn_struct.pop()
            item1.concat(item2)
            afn_struct.append(item1)
        
        if i == "?":
            item2 = AFN(cont, cont+1, epsilon)
            cont = cont + 2
            item1 = afn_struct.pop()
            temp_afn = AFN(cont, cont+1, epsilon)
            temp_afn.unionOperator(item1,item2)
            afn_struct.append(temp_afn)
            cont = cont + 2
            
        if i == "*":
            temp_afn = afn_struct.pop()
            temp_afn.closure(cont,cont+1,epsilon)
            afn_struct.append(temp_afn)
            cont = cont + 2
        
        if i == "+":       
            item1 = afn_struct.pop()
            finalNode = item1.getFinal()
            item1Node = item1.getInitial()
            item2 = AFN((finalNode+finalNode)-(finalNode-item1Node), finalNode+finalNode, item1.getLabel())
            item2.createCopy(item1.getDict(),finalNode)
            cont = item2.getFinal() + 1 
            item2.closure(cont,cont+1, epsilon)
            cont = cont + 2
            item1.concat(item2)
            afn_struct.append(item1)

    return afn_struct.pop()