from types import NoneType

from RustCode.AST_Scripts import AbstractProgramVisitor


class QXTop:

    def accept(self, visitor):
        pass


class QXStmt(QXTop):

    def accept(self, visitor: AbstractProgramVisitor):
        pass

class QXExp(QXTop):

    def accept(self, visitor: AbstractProgramVisitor):
        pass

class QXProgram(QXTop):
    def __init__(self, exps: [QXStmt]):
        self.exps = exps

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitProgram(self)

    def stmt(self, i: int = None):
        return self.exps[i] if len(self.exps) > i else None


class QXType(QXTop):

    def accept(self, visitor: AbstractProgramVisitor):
        pass


class QXBlock(QXStmt):
    def __init__(self, program: QXProgram):
        self.program = program

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitBlock(self)

    def program(self):
        return self.program


class QXVExp(QXExp):

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visit(self)

class QXIDExp(QXVExp):
    def __init__(self, id: str, type: QXType = None):
        self.id = id
        self.type = type

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitIDExp(self)

    def ID(self):
        return self.id if self.id is str else self.id.getText()

    def type(self):
        return self.type


class QXLet(QXStmt):
    def __init__(self, id: str, p: QXExp):
        self.id = id
        self.exp = p

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitLet(self)

    def ID(self):
        return self.id if isinstance(self.id, str) else self.id.getText()

    def exp(self):
        return self.exp


class QXPrint(QXStmt):
    def __init__(self, s: str, vs: QXExp):
        self.s = s
        self.vs = vs

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitPrint(self)

    def str(self) -> str:
        return self.s if isinstance(self.id, str) else self.s.getText()

    def exp(self):
        return self.vs


class QXIf(QXStmt):
    def __init__(self, v: QXVExp, left: QXBlock, right: QXBlock):
        self.v = v
        self.left = left
        self.right = right

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitIfStmt(self)

    def vexp(self):
        return self.v

    def left(self):
        return self.left

    def right(self):
        return self.right


class QXBreak(QXStmt):
    def __init__(self, v: QXVExp=None):
        self.v = v

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitBreak(self)

    def vexp(self):
        return self.v


class QXReturn(QXStmt):
    def __init__(self, v: QXVExp=None):
        self.v = v

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitReturn(self)

    def vexp(self):
        return self.v


class QXLoop(QXStmt):
    def __init__(self, s: QXBlock):
        self.s = s

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitLoop(self)

    def block(self):
        return self.s


class QXFor(QXStmt):
    def __init__(self, id: str, v: QXVExp, b:QXBlock):
        self.id = id
        self.v = v
        self.b = b

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitFor(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v

    def block(self):
        return self.b


class QXBin(QXVExp):
    def __init__(self, op: str, v1: QXVExp, v2: QXVExp):
        self.op = op
        self.v1 = v1
        self.v2 = v2

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitBin(self)

    def OP(self):
        return self.op

    def left(self):
        return self.v1

    def right(self):
        return self.v2


class QXString(QXVExp):
    def __init__(self, v: str):
        self.v = v

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitString(self)

    def str(self):
        return self.v


class QXBool(QXVExp):
    def __init__(self, v: bool):
        self.v = v

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitBool(self)

    def bool(self):
        return self.v

class QXNum(QXVExp):
    def __init__(self, v: int):
        self.v = v

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitNum(self)

    def num(self):
        return self.v

class Bool(QXType):
    type = "Bool"

    def type(self):
        return "Bool"

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitBoolType(self)


class Int(QXType):
    type = "Nat"

    def type(self):
        return "Nat"

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitInt(self)


class Fun(QXType):

    def __init__(self, args: [str], pre: dict, out: dict):
        self.args = args
        self.pre = pre
        self.out = out
        # self.r2 = r2

    def type(self):
        return ("Fun", (self.args, self.pre, self.out))

    def args(self):
        return self.args

    def pre(self):
        return self.pre

    def out(self):
        return self.out

    def __str__(self):
        return f"Fun(args={self.args}, pre={self.pre}, out={self.out})"

    def accept(self, visitor: AbstractProgramVisitor):
        visitor.visitFun(self)
