from typing import List, Tuple, Any, Dict

from language_templates.language import Language
from jinja2 import Template

SOLUTION_TEMPLATE = Template(
    """
const {{funcName}} = async ({{arguments}}) => {
{{body}}
    return (
        <div>Type your solution here</div>
    )
}
"""
)

CALL_TEMPLATE = Template("""{{funcName}}({{arguments}})""")


class React(Language):
    def codeComment(self, s: str):
        return f"// {s}"

    def codeArg(self, argName: str, argType: str):
        return argName

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        return SOLUTION_TEMPLATE.render(
            needsListType=needsListType,
            funcName=funcName,
            arguments=arguments,
            returnType=returnType,
            body=self.indent(body, 1),
        )

    def codeCall(self, funcName: str, arguments: str):
        return CALL_TEMPLATE.render(funcName=funcName, arguments=arguments)
