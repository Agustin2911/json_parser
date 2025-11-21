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

    "data/json_file9.json",
    "data/json_file10.json",
    "data/json_file11.json",
    "data/json_file12.json",
    "data/json_file13.json",
    "data/json_file14.json",
    "data/json_file15.json",
    "data/json_file16.json",
]

@pytest.mark.parametrize("path", JSON_FILES)
def test_full_parser(path):
    with open(path, "r", encoding="utf-8") as f:
        expected = json.load(f)

    tk = tokenizer()
    tokens = tk.tokenizer(path)

    tree = ast()
    tree.add(tokens)
    result = tree.convert_tree_to_dict()

    assert result == expected, f"❌ Fallo en {path}"



INVALID_JSON_FILES = [
    "data/invalid_json1.json",
    "data/invalid_json2.json",
    "data/invalid_json3.json",
    "data/invalid_json4.json",
    "data/invalid_json5.json",
    "data/invalid_json6.json",
    "data/invalid_json7.json",
    "data/invalid_json8.json",
    "data/invalid_json9.json",
    "data/invalid_json10.json",
    "data/invalid_json11.json",
    "data/invalid_json12.json",
    "data/invalid_json13.json",
    "data/invalid_json14.json",
    "data/invalid_json15.json",
    "data/invalid_json16.json",
    "data/invalid_json17.json",
    "data/invalid_json18.json",
    "data/invalid_json19.json",
    "data/invalid_json20.json",
]


@pytest.mark.parametrize("path", INVALID_JSON_FILES)
def test_invalid_json(path):
    tk = tokenizer()

    with pytest.raises(Exception):
        tokens = tk.tokenizer(path)
        tree = ast()
        tree.add(tokens)
        tree.convert_tree_to_dict()

