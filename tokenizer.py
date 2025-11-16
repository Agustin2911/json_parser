class tokenizer:

    def __init__(self) -> None:
       
        self.tokens=[]  # matrix with the following format : [type,value]
        self.open_quotes=False
        self.open_int=False
        self.open_boolean=False
        self.open_null=False 

    def tokenizer(self,path):   
        
        open_value=""
        
        with open(path,"r",encoding="utf-8") as open_file:
            
            for row in open_file:

                for char in row:
                    

                    # detects if the char is the beginning of string or an integer or a float
                    if char=='"':

                        self.open_quotes=not self.open_quotes
                        
                        if not self.open_quotes:
                            self.tokens.append(["string",open_value])
                            open_value=""
                    
                    elif char in ["1","2","3","4","5","6","7","8","9","0"]:

                            self.open_int= True
                             

                    elif char not in ["1","2","3","4","5","6","7","8","9","0","."] and self.open_int:
                            
                            self.open_int=False
                            if "." in open_value:
                                
                                self.tokens.append(["float",open_value])
                            else:       
                                self.tokens.append(["int",open_value])

                            open_value=""

                    elif char=="f" or char=="t" and not self.open_quotes:
                        
                        self.open_boolean=True

                     

                    elif self.open_boolean and char=="e":

                        self.open_boolean=False

                        open_value+=char

                        self.tokens.append(["boolean",open_value])
                        
                        open_value=""
                    
                    elif not self.open_quotes and char=="n":
                        self.open_null=True
                    
                    elif self.open_null and char=="l":

                        self.open_null=False
                        self.tokens.append(["null",open_value+"ll"])
                        open_value="" 
                    

                    #this part looks for simbols
                    if not self.open_quotes and not self.open_int and not self.open_boolean and not self.open_null:
                    
                        if char=="[" or char=="]" or char=="{" or  char=="}":

                            self.tokens.append(["simbol",char])
                        
                        elif char==":" or char==",":
                            self.tokens.append(["separation_sign",char])

                    #this part saves and builds the string and the int 
                    elif char!='"':
                        open_value+=char
                    


        
        print(self.tokens)     
        
        self.tokens.clear()

parser=tokenizer()
parser.tokenizer("json_file.json")

print()
parser.tokenizer("json_file2.json")

print()
parser.tokenizer("json_file3.json")
print()
parser.tokenizer("json_file4.json")
