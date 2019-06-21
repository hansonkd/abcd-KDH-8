from typing import List, Tuple, Any, Dict


class Language:
    INDENTATION = "    "

    def getSolutionTemplate(self, input: List[Dict[str, Any]], output: Any):
        """
        Takes a signature (list of dicts) and returns the solution template.
        """
        return self.codeFunctionTemplate(
            "solution",
            self.formatArguments(input),
            self.formatType(output),
            self.codeComment("Write your solution here"),
        )

    def getRunTemplate(self, solution: str, input_sig: List[Dict[str, Any]]):
        """
        Takes a signature (list of dicts) and returns the solution template.
        """
        return self.codeFunctionTemplate(
            solution,
            self.codeCall(self.codeSolutionFunction(), self.formatCall(input_sig))
        )

    def indent(self, s: str, times: int):
        indent = self.INDENTATION * times
        return "\n".join([indent + line for line in s.splitlines()])

    def formatType(self, t: Any):
        if isinstance(t, list):
            inner = self.formatType(t[0])
            return self.typeList(inner)
        elif t == "Integer":
            return self.typeInteger()
        elif t == "String":
            return self.typeString()
        elif t == "Double" or t == "Number":
            return self.typeDouble()
        elif t == "Boolean":
            return self.typeBool()
        else:
            raise Exception(f"Unknown type {t}")

    def formatArguments(self, args: List[Dict[str, Any]]):
        out = []
        for x in args:
            (key, t) = list(x.items())[0]
            out.append(self.codeArg(key, self.formatType(t)))
        return self.codeCombineArgs(out)

    def formatCall(self, args: List[Dict[str, Any]]):
        out = []
        for x in args:
            key = list(x.keys())[0]
            out.append(self.codeAccess("inp", key))
        return self.codeCombineArgs(out)

    # To Implement
    def typeString(self):
        return ""

    def typeDouble(self):
        return ""

    def typeInteger(self):
        return ""

    def typeBool(self):
        return ""

    def typeList(self, inner: str):
        return ""

    def quicktypeCommand(self, fp: str, label: str):
        raise NotImplementedError

    def codeAccess(self, v: str, attr: str):
        return f"{v}.{attr}"

    def codeComment(self, s: str):
        raise NotImplementedError

    def codeArg(self, argName: str, argType: str):
        raise NotImplementedError

    def codeCombineArgs(self, args: List[str]):
        return ", ".join(args)

    def codeFunctionTemplate(
        self, funcName: str, arguments: str, returnType: str, body: str
    ):
        raise NotImplementedError

    def codeCall(self, funcName: str, arguments: str):
        raise NotImplementedError
