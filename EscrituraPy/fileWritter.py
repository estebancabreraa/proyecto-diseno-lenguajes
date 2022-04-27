import pickle

class fileWritter():

    def __init__(self, file):
        self.filename = open((file+'.py'), 'w+')
        self.tab = '    '
        self.tabCount = 0
        self.filename.write('#Scanner created with %s.ATG data'%file)
        self.filename.write("\n")

    def addArray(self, name, array):
        self.filename.write("\n")
        self.filename.write((self.tab*self.tabCount+name+" = []"))
        self.filename.write("\n")
        for i in array:
            self.filename.write((self.tab*self.tabCount+name+".append('"+i+"')"))
            self.filename.write("\n")
    
    def addDict(self, name, dictionary):
        self.filename.write((self.tab*self.tabCount + name + ' = '))
        print(dictionary,file =self.filename)

    def addString(self, name, value):
        self.filename.write("\n")
        self.filename.write((self.tab*self.tabCount+name+"= '"+value+"'"))
    
    def substractTab(self):
        self.tabCount = self.tabCount - 1
    
    def writeFor(self, sentence):
        self.filename.write("\n")
        self.filename.write(self.tab*self.tabCount+sentence)
        self.tabCount = self.tabCount + 1
    
    def writeIf(self, sentence):
        self.filename.write("\n")
        self.filename.write(self.tab*self.tabCount+sentence)
        self.tabCount = self.tabCount + 1
    
    def writeSentence(self, sentence):
        self.filename.write("\n")
        self.filename.write(self.tab*self.tabCount+sentence)
    
    def writeEnter(self):
        self.filename.write("\n")

    def writeImport(self, sentence):
        self.filename.write(self.tab*self.tabCount+sentence)
        self.filename.write("\n")
    
    def addTest(self, newDict):
        print(newDict,file =self.filename)