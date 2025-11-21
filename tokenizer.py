class tokenizer:

    def __init__(self) -> None:
       
        self.tokens=[]  # matrix with the following format : [type,value]
        self.open_quotes=False
        self.open_int=False
        self.open_boolean=False
        self.open_null=False 

    def tokenizer(self,path):   
        
        self.tokens.clear()
        open_value=""
        
        with open(path,"r",encoding="utf-8") as open_file:
            
            for row in open_file:

                for char in range(0,len(row)):
                    

                    if row[char].isalpha() and row[char] not in ["t","f","n"] and not self.open_null and not self.open_boolean and not self.open_quotes and not self.open_int:
                        raise Exception("ew")

                    # detects if the char is the beginning of string or an iaaaaaaaaaaaaaanteger or a float
                    if row[char]=='"' and row[char-1]!="\\" :
                        
                        self.open_quotes=not self.open_quotes

                        if not self.open_quotes:
                            print(row[char+1]) 

                            self.tokens.append(["string",open_value])
                            open_value=""
                    
                    elif row[char] in ["1","2","3","4","5","6","7","8","9","0","-"] and not self.open_quotes:

                            self.open_int= True
                             

                    elif  row[char] not in ["1","2","3","4","5","6","7","8","9","0","."] and self.open_int:
                            
                            self.open_int=False

                            if open_value.startswith("0") and open_value!="0" and not open_value.startswith("0."):
                                raise Exception("error in the Syntaxs of the file")

                            if "." in open_value:
                                
                                self.tokens.append(["float",open_value])
                            else:
                                self.tokens.append(["int",open_value])

                            open_value=""

                    elif  (row[char] =="f" or row[char] =="t" )and not self.open_quotes :
                        print(row[char])
                        print(not self.open_quotes)
                        self.open_boolean=True


                        

                    elif self.open_boolean and (open_value+row[char]=="true" or open_value+row[char]=="false"):#row[char]=="e":
                        

                        self.open_boolean=False

                        open_value+=row[char]
                        
                        self.tokens.append(["boolean",open_value])
                        
                        open_value=""
                    
                    elif not self.open_quotes and row[char]=="n":
                        self.open_null=True
                    
                    elif self.open_null and open_value+row[char]=="null":
        
                        self.open_null=False 
                        self.tokens.append(["null","null"])
                        open_value="" 
                    
                    #this part looks for simbols
                    if not self.open_quotes and not self.open_int and not self.open_boolean and not self.open_null:
                        

                        print(row[char])
                        if row[char]=="[" or row[char]=="]" or row[char]=="{" or  row[char]=="}":

                            self.tokens.append(["simbol",row[char]])
                        
                        elif row[char]==":" or row[char]==",":
                            self.tokens.append(["separation_sign",row[char]])
                    
                    #this part saves and builds the string and the int 
                    elif row[char]!='"' and row[char-1]!="\\":
                        open_value+=row[char]
                    
                    elif  row[char]=='"' and row[char-1]=="\\" :
                        open_value=open_value[:-1]
                        open_value+=row[char]


                    elif row[char]=="n" and row[char-1]=="\\":
                        open_value=open_value[:-1]
                        open_value+="\n"
                
        return self.tokens
