from typing import List, Any, Dict
import subprocess
import tempfile
import json
from language_templates.language import Language
from language_templates.languages.java import Java


def make_schema(args: List[Dict[str, Any]]):
    properties = {}
    for x in args:
        (key, t) = list(x.items())[0]
        properties[key] = signature_type_to_schema_type(t)
    return {
      "type": "object",
      "properties": properties
    }


def signature_type_to_schema_type(t):
    if isinstance(t, list):
        return {'type': 'array', 'items': signature_type_to_schema_type(t[0])}
    elif t == "Integer":
        return {'type': 'integer'}
    elif t == "String":
        return {'type': 'string'}
    elif t == "Double" or t == "Number":
        return {'type': 'number'}
    elif t == "Boolean":
        return {'type': 'boolean'}
    else:
        raise Exception(f"Unknown type {t}")


def generate_type_file(language: Language, signature: List[Dict[str, Any]], label: str):
    schema = make_schema(signature)
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(json.dumps(schema).encode('utf-8'))
        fp.seek(0)
        command = language.quicktypeCommand(fp.name, label)
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        if process.returncode != 0:
            raise Exception("Error generating quicktype {output}")
    return output

LANGUAGE_DICT = {
    'java': Java()
}

def get_language(language_id: str):
    return LANGUAGE_DICT[language_id]