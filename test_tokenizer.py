import pytest
from tokenizer import tokenizer

# --- FIXTURES Y HELPERS ---

@pytest.fixture
def parser():
    return tokenizer()

# --- TEST CASES COMPLETOS ---

def test_full_test1(parser):
    """
    Archivo: test1.json
    Contenido: { "nombre": "Joa", "edad": 21 }
    """
    result = parser.tokenizer("data/test1.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "nombre"], ["separation_sign", ":"], ["string", "Joa"], ["separation_sign", ","],
        ["string", "edad"], ["separation_sign", ":"], ["int", "21"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_test2(parser):
    """
    Archivo: test2.json
    Contenido: { "nums": [1, -4, 50], "ok": true }
    """
    result = parser.tokenizer("data/test2.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "nums"], ["separation_sign", ":"], ["simbol", "["],
        ["int", "1"], ["separation_sign", ","],
        ["int", "-4"], ["separation_sign", ","],
        ["int", "50"], ["simbol", "]"], ["separation_sign", ","],
        ["string", "ok"], ["separation_sign", ":"], ["boolean", "true"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_test3(parser):
    """
    Archivo: test3.json
    Contenido: { "mensaje": "hola mundo", "meta": null }
    """
    result = parser.tokenizer("data/test3.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "mensaje"], ["separation_sign", ":"], ["string", "hola mundo"], ["separation_sign", ","],
        ["string", "meta"], ["separation_sign", ":"], ["null", "null"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_json_file2(parser):
    """
    Archivo: json_file2.json
    Contenido: { "nombre": "Joa", "edad": 21, "activo": true, "puntaje": 9.5 }
    """
    result = parser.tokenizer("data/json_file2.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "nombre"], ["separation_sign", ":"], ["string", "Joa"], ["separation_sign", ","],
        ["string", "edad"], ["separation_sign", ":"], ["int", "21"], ["separation_sign", ","],
        ["string", "activo"], ["separation_sign", ":"], ["boolean", "true"], ["separation_sign", ","],
        ["string", "puntaje"], ["separation_sign", ":"], ["float", "9.5"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_json_file4(parser):
    """
    Archivo: json_file4.json (Espacios desordenados)
    Contenido: { "meta" : null, "temperaturas": [ 10, -5, 0, 22 ], "mensaje": "Hola     mundo   ", "valido": false, "datos": { "vacio": { } } }
    """
    result = parser.tokenizer("data/json_file4.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "meta"], ["separation_sign", ":"], ["null", "null"], ["separation_sign", ","],
        ["string", "temperaturas"], ["separation_sign", ":"], ["simbol", "["],
        ["int", "10"], ["separation_sign", ","],
        ["int", "-5"], ["separation_sign", ","],
        ["int", "0"], ["separation_sign", ","],
        ["int", "22"], ["simbol", "]"], ["separation_sign", ","],
        ["string", "mensaje"], ["separation_sign", ":"], ["string", "Hola     mundo   "], ["separation_sign", ","],
        ["string", "valido"], ["separation_sign", ":"], ["boolean", "false"], ["separation_sign", ","],
        ["string", "datos"], ["separation_sign", ":"], ["simbol", "{"],
        ["string", "vacio"], ["separation_sign", ":"], ["simbol", "{"], ["simbol", "}"],
        ["simbol", "}"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_json_file(parser):
    """
    Archivo: json_file.json (Estructura grande y anidada)
    """
    result = parser.tokenizer("data/json_file.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "nombre"], ["separation_sign", ":"], ["string", "Joa"], ["separation_sign", ","],
        ["string", "edad"], ["separation_sign", ":"], ["int", "18"], ["separation_sign", ","],
        ["string", "altura"], ["separation_sign", ":"], ["float", "1.80"], ["separation_sign", ","],
        ["string", "activo"], ["separation_sign", ":"], ["boolean", "false"], ["separation_sign", ","],
        ["string", "direccion"], ["separation_sign", ":"], ["null", "null"], ["separation_sign", ","],
        ["string", "skills"], ["separation_sign", ":"], ["simbol", "["],
        ["string", "python"], ["separation_sign", ","],
        ["string", "bash"], ["separation_sign", ","],
        ["string", "java"], ["simbol", "]"], ["separation_sign", ","],
        ["string", "proyectos"], ["separation_sign", ":"], ["simbol", "["],
        ["simbol", "{"], ["string", "id"], ["separation_sign", ":"], ["int", "1"], ["separation_sign", ","], ["string", "titulo"], ["separation_sign", ":"], ["string", "Parser JSON"], ["separation_sign", ","], ["string", "completo"], ["separation_sign", ":"], ["boolean", "false"], ["simbol", "}"], ["separation_sign", ","],
        ["simbol", "{"], ["string", "id"], ["separation_sign", ":"], ["int", "2"], ["separation_sign", ","], ["string", "titulo"], ["separation_sign", ":"], ["string", "Sistema de stock"], ["separation_sign", ","], ["string", "completo"], ["separation_sign", ":"], ["boolean", "true"], ["simbol", "}"],
        ["simbol", "]"],
        ["simbol", "}"]
    ]
    
    assert result == expected

def test_full_json_file3(parser):
    """
    Archivo: json_file3.json (Caracteres de escape y saltos de linea)
    NOTA: Este test espera que el string 'María \"La Pro\"' se tokenice correctamente como un solo string.
    """
    result = parser.tokenizer("data/json_file3.json")
    
    expected = [
        ["simbol", "{"],
        ["string", "usuarios"], ["separation_sign", ":"], ["simbol", "["],
        ["simbol", "{"],
        ["string", "id"], ["separation_sign", ":"], ["int", "1"], ["separation_sign", ","],
        # El siguiente string contiene comillas escapadas
        ["string", "nombre"], ["separation_sign", ":"], ["string", "María \"La Pro\""], ["separation_sign", ","],
        ["string", "roles"], ["separation_sign", ":"], ["simbol", "["], ["string", "admin"], ["separation_sign", ","], ["string", "editor"], ["simbol", "]"],
        ["simbol", "}"], ["separation_sign", ","],
        ["simbol", "{"],
        ["string", "id"], ["separation_sign", ":"], ["int", "2"], ["separation_sign", ","],
        # El siguiente string contiene un salto de linea
        ["string", "nombre"], ["separation_sign", ":"], ["string", "Fran\nElLoco"], ["separation_sign", ","],
        ["string", "roles"], ["separation_sign", ":"], ["simbol", "["], ["simbol", "]"],
        ["simbol", "}"],
        ["simbol", "]"], ["separation_sign", ","],
        ["string", "config"], ["separation_sign", ":"], ["simbol", "{"],
        ["string", "tema"], ["separation_sign", ":"], ["string", "oscuro"], ["separation_sign", ","],
        ["string", "reintentos"], ["separation_sign", ":"], ["int", "3"],
        ["simbol", "}"],
        ["simbol", "}"]
    ]
    
    assert result == expected
