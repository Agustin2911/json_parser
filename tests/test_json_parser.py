import json
import pytest
from json_parser_files.ast_tree import ast
from json_parser_files.tokenizer import tokenizer


JSON_FILES = [
    "tests/data/json_file1.json",
    "tests/data/json_file2.json",
    "tests/data/json_file3.json",
    "tests/data/json_file4.json",
    "tests/data/json_file5.json",
    "tests/data/json_file6.json",
    "tests/data/json_file7.json",
    "tests/data/json_file8.json",

    "tests/data/json_file9.json",
    "tests/data/json_file10.json",
    "tests/data/json_file11.json",
    "tests/data/json_file12.json",
    "tests/data/json_file13.json",
    "tests/data/json_file14.json",
    "tests/data/json_file15.json",
    "tests/data/json_file16.json",

    "tests/data/json_file17.json",
    "tests/data/json_file18.json",
    "tests/data/json_file19.json",
    "tests/data/json_file20.json",
    "tests/data/json_file21.json",
    "tests/data/json_file22.json",
    "tests/data/json_file23.json",
    "tests/data/json_file24.json",
    "tests/data/json_file25.json",
    "tests/data/json_file26.json",
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
    "tests/data/invalid_json1.json",
    "tests/data/invalid_json2.json",
    "tests/data/invalid_json3.json",
    "tests/data/invalid_json4.json",
    "tests/data/invalid_json5.json",
    "tests/data/invalid_json6.json",
    "tests/data/invalid_json7.json",
    "tests/data/invalid_json8.json",
    "tests/data/invalid_json9.json",
    "tests/data/invalid_json10.json",
    "tests/data/invalid_json11.json",
    "tests/data/invalid_json12.json",
    "tests/data/invalid_json13.json",
    "tests/data/invalid_json14.json",
    "tests/data/invalid_json15.json",
    "tests/data/invalid_json16.json",
    "tests/data/invalid_json17.json",
    "tests/data/invalid_json18.json",
    "tests/data/invalid_json19.json",
    "tests/data/invalid_json20.json",
    "tests/data/invalid_json21.json",
    "tests/data/invalid_json22.json",
    "tests/data/invalid_json23.json",
    "tests/data/invalid_json24.json",
    "tests/data/invalid_json25.json",
    "tests/data/invalid_json26.json",
    "tests/data/invalid_json27.json",
    "tests/data/invalid_json28.json",
    "tests/data/invalid_json29.json",
    "tests/data/invalid_json30.json",
]


@pytest.mark.parametrize("path", INVALID_JSON_FILES)
def test_invalid_json(path):
    tk = tokenizer()

    with pytest.raises(Exception):
        tokens = tk.tokenizer(path)
        tree = ast()
        tree.add(tokens)
        tree.convert_tree_to_dict()

