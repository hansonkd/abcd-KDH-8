from typing import List, Tuple, Any, Dict

from language_templates.language import Language
from jinja2 import Template

SOLUTION_TEMPLATE = Template(
    """
class Solution {
    public static {{returnType}} {{funcName}}({{arguments}}) {
{{body}}
    }
}
"""
)

RUN_TEMPLATE = Template(
    """
{{solution}}

class Main {
    public static void main(String[] args) throws Throwable {
        String input = "";
        java.util.Scanner scanner = new java.util.Scanner(System.in).useDelimiter("\\n");
        while (scanner.hasNext()) {
            input += scanner.next();
        }

        io.inputtypes.Input inp = io.inputtypes.InputFromJsonString(input)
        System.out.println(io.outputtypesOutputToJsonString({{ call_function }}));
    }
}
"""
)

CALL_TEMPLATE = Template("""{{funcName}}({{arguments}})""")

COMPILE_COMMAND_TEMPLATE = Template("javac -cp /support/jackson-databind-2.9.9.jar {{ main_file }} {{ otherfiles|join(" ") }}")

RUN_COMMAND_TEMPLATE = Template("java Main")


class Java(Language):
    def typeString(self):
        return "String"

    def typeDouble(self):
        return "double"

    def typeInteger(self):
        return "long"

    def typeList(self, inner: str):
        return f"{inner}[]"

    def typeBool(self):
        return "boolean"

    def quicktypeCommand(self, fp: str, label: str):
        return ['quicktype', '-s', 'schema', fp, '-l', 'java', '--package', f'compiletasks.{label}']

    def codeSolutionFunction(self):
        return f"Solution.solution"

    def codeComment(self, s: str):
        return f"// {s}"

    def codeArg(self, argName: str, argType: str):
        return f"{argType} {argName}"

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        return SOLUTION_TEMPLATE.render(
            funcName=funcName,
            arguments=arguments,
            returnType=returnType,
            body=self.indent(body, 2),
        )

    def codeRunTemplate(self, solution: str, call_function: str):
        return RUN_TEMPLATE.render(solution=solution, call_function=call_function)

    def codeCall(self, funcName: str, arguments: str):
        return CALL_TEMPLATE.render(funcName=funcName, arguments=arguments)
