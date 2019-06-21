from language_templates.language import Language


class Sql(Language):
    def codeComment(self, s: str):
        return f"/* {s} */"

    def codeArg(self, argName: str, argType: str):
        return ""

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        return body

    def codeCall(self, funcName: str, arguments: str):
        raise NotImplementedError
