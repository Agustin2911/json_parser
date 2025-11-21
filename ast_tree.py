from array_node import array_node
from object_node import object_node
from leaf import leaf

class ast:
    
    def __init__(self): 

        self.root=None

    def add(self,tokens):
        
        object_tokens=[]
        token_value=""
        inserted=False 
        pointer=self.root
        
        for value in tokens:
            if value[1]=="{":
            
                token_value=object_node()
            
            elif value[1]=="[":
                token_value=array_node()

            elif value[0]=="null" or value[0]=="string" or value[0]=="int" or value[0]=="boolean":
                inserted=True
                token_value=leaf(value[0],value[1])

            
            if self.root==None:
                self.root=token_value
                pointer=self.root

            elif (token_value.type=="array" or token_value.type=="object"):
                

                token_value.setFather(pointer)

                if pointer.type=="array":
                    pointer.add(token_value)
                
                elif pointer.type=="object":
                    print(object_tokens[0].value)
                    pointer.add(object_tokens[0],token_value)
                    object_tokens=[]

                pointer=token_value

            elif pointer.type=="array" and value[1]=="]":
                pointer=pointer.father
            
        
            elif pointer.type=="object" and value[1]=="}" and pointer.father!=None:
                pointer=pointer.father


            elif pointer.type=="array" and value[0] =="simbol" and (value[1]=="}"):
                raise Exception(f"wrong syntaxs {value[1]} pointer type: {pointer.type}")

            elif pointer.type=="object" and value[0] =="simbol" and (value[1]=="]"):
                raise Exception(f"wrong syntaxs {value[1]} pointer type: {pointer.type}")

            elif pointer.type=="array" and (token_value.type=="boolean" or token_value.type=="null" or token_value.type=="string" or token_value.type=="int") and inserted==True:
    
                pointer.add(token_value)
                inserted=False


                        
            elif pointer.type=="object" and inserted:

                if len(object_tokens)==0:
                    object_tokens.append(token_value)

                elif len(object_tokens)==1 :
                    object_tokens.append(token_value)
                    pointer.add(object_tokens[0],object_tokens[1])
                    object_tokens=[]
                
                inserted=False

        try:     
            if (pointer.type=="object" and value[1]!="}" )or (pointer.type=="array" and value[1]!="]"):
                raise Exception("Syntaxs error , json has never been closed")
        except AttributeError as e:
            pass
    def print(self):

        if self.root.type=="array":
            self.print_list(self.root.nodes)
        else:
            self.print_object(self.root.nodes)

    def print_list(self,list):

        for i in list:
            
            if i.type in ["int","string","boolean","null","float"]:
                print(i.value)

            elif  i.type=="array":
                self.print_list(i.nodes)
            
            elif i.type=="object":
                self.print_object(i.nodes)


    def print_object(self,list):
        
        for i,y in list.items():
            
            if y.type=="object":
                print(i.value,":")
                self.print_object(y.nodes)
            elif y.type=="array":
                print(i.value,":")
                self.print_list(y.nodes)
            else:
                print(i.value,":",y.value)


    def convert_tree_to_dict(self):
        
        if self.root.type=="object":
            return self.add_data_to_the_dict_from_a_object(self.root.nodes)

        elif self.root.type=="array":

            return self.add_data_to_the_dict_from_a_list(self.root.nodes)

    def convert_the_token_to_the_correct_data_type(self,token):
        try:
            if token.type=="int":
                return int(token.value)
            elif token.type=="string":
                return str(token.value)
            elif token.type=="float":
                return float(token.value)
            elif token.type=="boolean" and token.value=="true":
                return True
            elif token.type=="boolean" and token.value=="false":
                return False
            elif token.type=="null":
                return None

        except Exception as e:
            print(e)
            raise Exception("error at convertin a token to the right data type")

    def add_data_to_the_dict_from_a_list(self,list_of_tokens):
        
        list=[]
        for i in list_of_tokens:
            
            if i.type in ["int","string","boolean","null","float"]:
                value=self.convert_the_token_to_the_correct_data_type(i)
                list.append(value)

            elif  i.type=="array":
                list.append(self.add_data_to_the_dict_from_a_list(i.nodes))
            
            elif i.type=="object":
               list.append(self.add_data_to_the_dict_from_a_object(i.nodes))
        
        return list


    def add_data_to_the_dict_from_a_object(self,dict_of_tokens):
        dict={} 
        for i,y in dict_of_tokens.items():
            print(i.type)
            print(y.type)
            if i.type!="string":
                
                raise Exception(f"Error at the syntaxis of the json file , a key it cant not be a {i.type}")
            
            if y.type=="object":
                
                print(i.value)
                print(len(y.nodes))
                key_value=self.convert_the_token_to_the_correct_data_type(i)

                child_dict=self.add_data_to_the_dict_from_a_object(y.nodes)
                
                dict[key_value]=child_dict

            elif y.type=="array":
                key_value=self.convert_the_token_to_the_correct_data_type(i)

                child_dict=self.add_data_to_the_dict_from_a_list(y.nodes)
                
                dict[key_value]=child_dict
            else:
                
                key=self.convert_the_token_to_the_correct_data_type(i)
                value=self.convert_the_token_to_the_correct_data_type(y)
                dict[key]=value
        
        print(dict)
        return dict
