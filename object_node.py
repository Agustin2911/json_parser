class object_node:


    def __init__(self):
        
        self.nodes={}
        self.type="object"
        self.father=None

    def add(self,key,value):

        self.nodes[key]=value

    def setFather(self,father):
        self.father=father
