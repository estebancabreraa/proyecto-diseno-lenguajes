from classes.postfix import *
from classes.algoritmo_thompson import ThompsonAlgorithm
from classes.graph import graph
from classes.graphDirect import graphDirect
from classes.subnets import eCerradura, subsetsBuilder
from classes.simulaciones import simulationAFN, simulationAFD
from classes.afd import buildAFD

header = '''######################################################################################
#                            Proyecto # 1 Diseno de lenguajes                        #
######################################################################################'''
afn_header = '''######################################################################################
#                            Creacion de AFN y AFD                                   #
######################################################################################'''
afd_header = '''######################################################################################
#                            Creacion de AFD DIRECTO                                 #
######################################################################################'''
menu = '''######################################################################################

\n1. Creacion de AFN Y AFD.
2. AFD directo.
3. Salir.\n
######################################################################################\n
Ingrese la opcion deseada:
'''
stop = False
while not stop:
    print(header)
    option = input(menu)
    if not option == "3":
        expresion = input ("\nIngrese la expresión, por favor: ")
        if firstExpresion(expresion):
            if option == "1":
                print(afn_header)
                main_expresion = computableExpresion(expresion)
                print("Expresion ingresada: ",expresion)
                print("Expresion entendible para computadora: ", main_expresion)
                resultPostfix = infixaPostfix(main_expresion)
                print("Expresion en Postfix:", resultPostfix)
                resultThompson = ThompsonAlgorithm(resultPostfix)
                nfaDict = resultThompson.getDict()
                finalGraph = graph(resultPostfix, resultThompson)
                transitions = finalGraph.createTransitions()
                finalGraph.graphic(transitions, "Resultado Thompson")
                initialState = resultThompson.getInitial()
                finalState = resultThompson.getFinal()
                states = finalGraph.getStates()
                alphabet = getAlphabet(expresion)
                dictTrans = resultThompson.getDict()
                subsets, numberSubsets, subsetsInfo, finalNodeInside = subsetsBuilder(alphabet, states, dictTrans, initialState, finalState)
                finalGraph.graphSubsets(subsets, numberSubsets,"Resultado Subconjuntos", finalNodeInside) 

                simulation_stop = False
                while not simulation_stop:
                    segundaExpresion = input ("\n------------- Nueva Simulación -------------\nIngrese la expresión a evaluar, por favor:\n>> ")
                    resultSimNFA = simulationAFN(dictTrans, initialState, finalState, segundaExpresion, subsetsInfo, alphabet)
                    print("Simulación de AFN: ", resultSimNFA)
                    resultSimFDA = simulationAFD(subsets, numberSubsets, segundaExpresion, alphabet)
                    print("Simulación de AFD: ", resultSimNFA)
                    option = input ("¿Desea realizar otra simulacion?\n1.Sí\n2.No\n ")
                    if option == "2":
                        simulation_stop= True

            elif option == "2":
                print(afd_header)
                expresion = convertOperators(expresion)
                print(expresion)
                main_expresionComputable = computableExpresion(expresion)
                resultPostfixNueva = infixaPostfix(main_expresionComputable)+["#","_"]
                print("Expresion que con la que se hará el arbol sintactico ",resultPostfixNueva)
                labelsDstates, acceptance = buildAFD(resultPostfixNueva)
                finalGraph = graphDirect(acceptance, labelsDstates, "AFD directo")
            else:
                print("La opcion indicada no existe.")
        else: 
            print("La expresion que ingreso contiene errores.")
    else: 
        stop = True
        print("<<<<<FIN>>>>>>")