class queue:

    def __init__(self):
       
        self.queue=[]
        self.lenght=0

    def add (self,type):
        
        self.queue.append(type)
        self.lenght+=1

    def delete(self):
        del self.queue[self.lenght-1]
        self.lenght-=1

    def first(self):

        return self.queue[self.lenght-1]
    
    def emptyqueue(self):

        return self.lenght==0
        
