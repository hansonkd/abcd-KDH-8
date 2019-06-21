from typing import List, Tuple, Any, Dict

from language_templates.language import Language
from jinja2 import Template

SOLUTION_TEMPLATE = Template(
    """
@implementation Challenge

- ({{returnType}}){{funcName}}:{{arguments}} {
{{body}}
}

@end
"""
)

CALL_TEMPLATE = Template("""{{funcName}}[{{arguments}}]""")


class ObjC(Language):
    def typeString(self):
        return "NSString *"

    def typeDouble(self):
        return "double"

    def typeInteger(self):
        return "NSInteger"

    def typeList(self, inner: str):
        return f"NSArray *"

    def typeBool(self):
        return "BOOL"

    def codeComment(self, s: str):
        return f"// {s}"

    def codeArg(self, argName: str, argType: str):
        return "(" + argType + ")" + argName

    def codeCombineArgs(self, arguments):
        return ":".join(arguments)

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
