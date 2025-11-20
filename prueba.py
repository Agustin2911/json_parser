from tokenizer import  tokenizer
from ast import ast
token=tokenizer()
tokens=token.tokenizer("data/json_file6.json")
ast_tree=ast()
ast_tree.add(tokens)
print(ast_tree.convert_tree_to_dict())
