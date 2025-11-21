from tokenizer import  tokenizer
from ast_tree import ast
token=tokenizer()
tokens=token.tokenizer("data/json_file7.json")
print(tokens)
print()
print()
ast_tree=ast()
ast_tree.add(tokens)
#ast_tree.print()
print()
print()
print(ast_tree.convert_tree_to_dict())
