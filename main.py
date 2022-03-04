from classes.postfix import *
from classes.algoritmo_thompson import ThompsonAlgorithm
from classes.graph import graph
from classes.graphDirect import graphDirect
from classes.subnets import eCerradura, subsetsBuilder
from classes.simulaciones import simulationNFA, simulationFDA
from classes.afd import buildAFD

menu = '''######################################################################################

\n1. Creacion de AFN Y AFD.
2. AFD directo.
3. Salir.\n
######################################################################################\n
Ingrese la opcion deseada:
'''
stop = False
while not stop:
    option = input(menu)
    if not option == "3":
        expresion = input ("\nIngrese la expresión, por favor: ")
        if firstExpresion(expresion):
            if option == "1":
                print("---------- CREACIÓN AFN Y AFD ----------")
                nuevaexpresion = computableExpresion(expresion)
                print("Expresion ingresada: ",expresion)
                print("Expresion entendible para computadora: ",nuevaexpresion)
                resultPostfix = infixaPostfix(nuevaexpresion)
                print("Expresion en Postfix:", resultPostfix)
                resultThompson = ThompsonAlgorithm(resultPostfix)
                nfaDict = resultThompson.getDict()
                #print("Dict con el A resultante:\n",nfaDict)
                finalGraph = graph(resultPostfix, resultThompson)
                transitions = finalGraph.createTransitions()
                finalGraph.graphic(transitions, "Thompson")
                initialState = resultThompson.getInitial()
                finalState = resultThompson.getFinal()
                states = finalGraph.getStates()
                #print("Nodo inicial: ",initialState,"\nNodo de aceptación/final: ",finalState)
                alphabet = getAlphabet(expresion)
                dictTrans = resultThompson.getDict()
                subsets, numberSubsets, subsetsInfo, finalNodeInside = subsetsBuilder(alphabet, states, dictTrans, initialState, finalState)
                finalGraph.graphSubsets(subsets,numberSubsets,"Subconjuntos",finalNodeInside) 
                simulation = True
                while simulation:
                    segundaExpresion = input ("\n------------- Nueva Simulación -------------\nIngrese la expresión a evaluar, por favor:\n>> ")
                    resultSimNFA = simulationNFA(dictTrans, initialState, finalState, segundaExpresion, subsetsInfo, alphabet)
                    print("Resultado de la simulación AFN: ", resultSimNFA)
                    resultSimFDA = simulationFDA(subsets, numberSubsets, segundaExpresion, alphabet)
                    print("Resultado de la simulación AFD: ", resultSimNFA)
                    option = input ("¿Desea realizar otra simulacion?\n1.Sí   2.No\n>> ")
                    if option == "2":
                        simulation = False
            elif option == "2":
                print("---------- CREACIÓN AFD DIRECTO ----------")
                expresion = convertOperators(expresion)
                print(expresion)
                nuevaExpresionComputable = computableExpresion(expresion)
                resultPostfixNueva = infixaPostfix(nuevaExpresionComputable)+["#","_"]
                print("Expresion que con la que se hará el arbol sintactico ",resultPostfixNueva)
                labelsDstates, acceptance = buildAFD(resultPostfixNueva)
                finalGraph = graphDirect(acceptance, labelsDstates, "AFD directo")
            else:
                print("Opcion equivocada")
        else: 
            print("La expresion tiene errores")
    else: 
        stop = True
        print("ADIOS, gracias por usarme :)")