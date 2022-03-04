from classes.afn import *

epsilon = 'ε'

def validChar(char):
    if char in ["*","?","|","_","+"]:
        return False

    elif char == "ε":
        return True

    elif char.isalpha():
        return True

    elif char.isnumeric():
        return True  

    else: 
        return False

def ThompsonAlgorithm(postfixexp):
    nfaStack = []
    cont = 1
    
    for i in postfixexp:
        if (validChar(i)):
            nfaStack.append(AFN(cont, cont+1,i))
            cont = cont + 2

        if i == "|":
            temp = AFN(cont, cont+1, epsilon)
            second = nfaStack.pop()
            first = nfaStack.pop()
            temp.unionOperator(first,second)
            nfaStack.append(temp)
            cont = cont + 2

        if i == "_":
            second = nfaStack.pop()
            first = nfaStack.pop()
            first.concat(second)
            nfaStack.append(first)
        
        if i == "?":
            second = AFN(cont, cont+1, epsilon)
            cont = cont + 2
            first = nfaStack.pop()
            temp = AFN(cont, cont+1, epsilon)
            temp.unionOperator(first,second)
            nfaStack.append(temp)
            cont = cont + 2
            
        if i == "*":
            temp = nfaStack.pop()
            temp.closure(cont,cont+1,epsilon)
            nfaStack.append(temp)
            cont = cont + 2
        
        if i == "+":       
            first = nfaStack.pop()
            finalNode = first.getFinal()
            firstNode = first.getInitial()
            second = AFN((finalNode+finalNode)-(finalNode-firstNode), finalNode+finalNode, first.getLabel())
            second.createCopy(first.getDict(),finalNode)
            cont = second.getFinal() + 1 
            second.closure(cont,cont+1, epsilon)
            cont = cont + 2
            first.concat(second)
            nfaStack.append(first)

    return nfaStack.pop()