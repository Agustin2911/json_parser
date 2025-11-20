
class array_node:

    def __init__(self) :
        self.nodes=[] 
        self.type="array"
        self.father=None

    def add(self,value):
        self.nodes.append(value)

    def setFather(self,father):
        self.father=father
