import string

from objects import Equation
from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY
from notation import infix_to_postfix


def get_var_to_one_side(sides, Eq):
    has_x = []
    for i, expression in enumerate(sides):
        if Eq.var in expression:
            has_x.append(i)

    if len(has_x) == 1:
        return sides


Eq = Equation("1-1x*4=1/(2*2)+(2x^4+4)/2", 'x')
Eq.verify()

decomosedEq = Eq.decompose()
sides = []
for side in decomosedEq:
    print("Side: ", side)
    sides.append(infix_to_postfix(side, Eq.var))

# sides = infix_to_postfix(decomosedEq, Eq.var)



print(get_var_to_one_side(sides, Eq))
