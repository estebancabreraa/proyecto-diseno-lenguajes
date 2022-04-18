def eCerradura(dictionary, finalNode, node):
    if not finalNode == node:
        falseStates = []
        if type(node) == list:
            for i in node:
                falseStates.append(i)
        else:
            falseStates.append(node)
        for i in falseStates:
            if not i == finalNode:
                subDict = dictionary[i]
                key = list(subDict.keys())
                if key[0] == "ε":
                    values = list(subDict.values())[0]
                    if type(values) == list:
                        for k in values:
                            if k not in falseStates:
                                falseStates.append(k)
                    else:
                        if values not in falseStates:
                            falseStates.append(values)
        print(falseStates)
        return falseStates

def move(dictionary, finalNode,states,label):
    result=[]
    for i in states:
        if not i == finalNode:
            subDict = dictionary[i]
            key = list(subDict.keys())[0]
            if key == label:
                values = list(subDict.values())[0]
                if type(values) == list:
                    for k in values:
                        result.append(k)
                else:
                    result.append(values)
    temp = []

    for i in result:
        temp.append(eCerradura(dictionary,finalNode,i))
    for i in temp:
        if type(i) == list:
            for j in i:
                result.append(j)
        elif i == None:
            pass
        else:
            result.append(i)
    return list(set(result))

def simulationAFN(dictionary, initial, final, expresion, subsets,alphabet):
    S = []
    S.append(sorted(eCerradura(dictionary, final, initial)))
    cont = 0
    for i in expresion:
        if i in alphabet:
            S.append(sorted(move(dictionary, final, S[cont], i)))
            cont = cont +1 
        else: 
            return "No"
    if subsets[len(subsets)-1] in S:
        return "Sí"
    else:
        return "No"

def simulationAFD(subsetsTrans, states, expresion, alphabet):
    S = []
    currentState = states[0]
    for i in expresion:
        if i in alphabet:
            flag = False
            for j in subsetsTrans:
                if j[0] == currentState and j[2] == i:
                    flag = True
                    S.append(j[1])
                    currentState = j[1]
            if not flag:
                return "No"
        else:
            return "No"
    if states[len(states)-1] in S:
        return "Sí"
    else:
        return "No"