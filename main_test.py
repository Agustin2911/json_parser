from json_parser_files.tokenizer import tokenizer
from json_parser_files.ast_tree import ast

json_tokenizer=tokenizer()
toknes=json_tokenizer.tokenizer("tests/data/json_file8.json")

print("Resultado tokenizer--------------------------")
print()

print()
print()
print()
print(toknes)
print()
print()
print()
print()
ast_tree=ast()
ast_tree.add(toknes)

print("Resultado final------------------------------")

print()
print()
print()
print()
print(ast_tree.convert_tree_to_dict())
