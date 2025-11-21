import json
import pytest
from tokenizer import tokenizer
from ast_tree import ast
JSON_FILES = [
    "data/json_file1.json",
    "data/json_file2.json",
    "data/json_file3.json",
    "data/json_file4.json",
    "data/json_file5.json",
    "data/json_file6.json",
    "data/json_file7.json",
    "data/json_file8.json",
]

@pytest.mark.parametrize("path", JSON_FILES)
def test_full_parser(path):
    # Cargar JSON real con json.load()
    with open(path, "r", encoding="utf-8") as f:
        expected = json.load(f)

    # Tu flujo real: tokenizer → AST → dict
    tk = tokenizer()
    tokens = tk.tokenizer(path)

    tree = ast()
    tree.add(tokens)
    result = tree.convert_tree_to_dict()

    assert result == expected, f"Fallo en {path}"

