class node:
    
    def __init__(self):

        self.left=None
        self.right=None

    def setKey(self,key):
        self.left=key

    def getKey(self):
        return self.left
    
        
    def setValue(self,value):
        self.right=value

    def getValue(self):
        return self.right
    
