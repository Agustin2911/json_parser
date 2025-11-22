<h1 align="center">JSON Parser </h1>

<p align="center">
Un proyecto educativo donde construí desde cero un parser JSON, incluyendo un tokenizer, un árbol AST y un sistema completo de validación.  
</p>

---

## 📘 Descripción del proyecto (Español)

Este proyecto nace de una curiosidad: entender cómo funcionan realmente los *parsers* debajo de la superficie.  
En Python solemos usar `json.load()` sin pensar demasiado en lo que ocurre internamente. Para aprender más, decidí **replicar el funcionamiento de un parser JSON desde cero**, construyendo:

- Un **tokenizer** que lee carácter por carácter y los transforma en tokens del tipo:  
  `["tipo_de_dato", "valor"]`
- Un **árbol AST (Abstract Syntax Tree)** que interpreta los tokens, valida la estructura y crea un árbol semántico.
- Un método final `convert_tree_to_dict()` que transforma dicho árbol en un diccionario de Python con los tipos correctos.

Luego, para asegurar que el resultado fuera confiable, utilicé **pytest** para crear una batería completa de casos de prueba:
- JSON correctos de diferentes tamaños y estructuras  
- JSON incorrectos, con errores de sintaxis  

Esto permitió validar la solidez del parser, detectar errores y asegurar un comportamiento consistente.

---

## 📘 Project Description (English)

This project was born out of curiosity: understanding how parsers actually work under the hood.  
In Python, we often rely on `json.load()` without thinking about the steps required to turn raw text into structured data.  
To learn more about this process, I built a **JSON parser from scratch**, including:

- A **tokenizer** that reads characters and transforms them into tokens like:  
  `["data_type", "value"]`
- An **AST (Abstract Syntax Tree)** that interprets tokens, validates structure, and builds a semantic tree.
- A final method `convert_tree_to_dict()` that converts the AST into a real Python dictionary with correct data types.

To ensure correctness, I used **pytest** with multiple test cases:
- Valid JSON files with different structures  
- Invalid JSON files with syntactic errors  

This testing process guarantees that the parser behaves consistently and handles incorrect input properly.

---

# ⚙️ Cómo instalar y ejecutar el proyecto

A continuación se explica cómo clonar el proyecto, crear un entorno virtual e instalar dependencias.  
Puedes hacerlo en **Windows**, **Linux** o **macOS**.

---

## 📥 1. Clonar el repositorio

```bash
git clone git@github.com:Agustin2911/json_parser.git
cd json_parser

#linux and macos set up
python3 -m venv .env
source .env/bin/activate
pip3 install pytest

#windows set up
python -m venv .env
.\.env\Scripts\activate
pip install pytest

PYTHONPATH=. pytest -vv tests/test_json_parser.py
