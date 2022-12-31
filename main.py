class person:
    def __init__(self,name):
        self.name = name
    def __getname(self):
        print(self.name)
    def getname(self):
        person.__getname(self)


mina = person("mina")
mina.getname()




