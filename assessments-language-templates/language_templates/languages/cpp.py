from typing import List, Tuple, Any, Dict

from language_templates.language import Language
from jinja2 import Template

SOLUTION_TEMPLATE = Template(
    """
#include <cctype>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

{{returnType}} {{funcName}}({{arguments}}) {
{{body}}
}

"""
)

CALL_TEMPLATE = Template("""{{funcName}}({{arguments}})""")


class CPP(Language):
    def typeString(self):
        return "string"

    def typeDouble(self):
        return "double"

    def typeInteger(self):
        return "long"

    def typeList(self, inner: str):
        return f"vector< {inner} >"

    def typeBool(self):
        return "bool"

    def codeComment(self, s: str):
        return f"// {s}"

    def codeArg(self, argName: str, argType: str):
        return f"{argType} {argName}"

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        return SOLUTION_TEMPLATE.render(
            funcName=funcName.capitalize(),
            arguments=arguments,
            returnType=returnType,
            body=self.indent(body, 2),
        )

    def codeCall(self, funcName: str, arguments: str):
        return CALL_TEMPLATE.render(funcName=funcName, arguments=arguments)
