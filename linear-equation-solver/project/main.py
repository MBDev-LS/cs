import string

from objects import Equation
from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY
from notation import infix_to_postfix


def lsplit(lst, item):
    try:
        index = lst.index(item)
        return [lst[:index], lst[index+1:]]
    except:
        return [lst, lst]


def get_var_to_one_side(sides, Eq):
    has_x = []
    for i, expression in enumerate(sides):
        if Eq.var in expression:
            has_x.append(i)

    if len(has_x) == 1:
        return sides


Eq = Equation("1x=1/(2*2)+(2^4+4)/2", 'x')
Eq.verify()

sides = infix_to_postfix(Eq)

print(get_var_to_one_side(sides, Eq))
