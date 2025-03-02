from typing import List, Tuple, Any, Dict

from language_templates.language import Language
from jinja2 import Template

SOLUTION_TEMPLATE = Template(
    """
package main

import "encoding/json"
import "fmt"

func {{funcName}}({{arguments}}) {{returnType}} {
{{body}}
}
"""
)

CALL_TEMPLATE = Template("""{{funcName}}({{arguments}})""")


class Golang(Language):
    def typeString(self):
        return "string"

    def typeDouble(self):
        return "float64"

    def typeInteger(self):
        return "int"

    def typeList(self, inner: str):
        return f"[]{inner}"

    def typeBool(self):
        return "bool"

    def codeComment(self, s: str):
        return f"// {s}"

    def codeArg(self, argName: str, argType: str):
        return f"{argName} {argType}"

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        return SOLUTION_TEMPLATE.render(
            funcName=funcName,
            arguments=arguments,
            returnType=returnType,
            body=self.indent(body, 1),
        )

    def codeCall(self, funcName: str, arguments: str):
        return CALL_TEMPLATE.render(funcName=funcName, arguments=arguments)
