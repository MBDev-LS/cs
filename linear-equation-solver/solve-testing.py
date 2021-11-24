import string
import math

equation = "x=1+1"


class Equation():
    def __init__(self):
        self.eq = "1x=1+x1"
        self.var = 'x'


class SubEq():
    def __init__(self, eq, var):
        self.eq = eq
        self.var = var


Eq = Equation()


def verify(eq):
    chars = []
    for c in eq.eq:
        if not c.isdigit() and c in string.ascii_lowercase:
            chars.append(c)
    if len(list(set(chars))) > 1:
        print('Thisprogram currently only supports equations with one unknown variable')
        return False

    if eq.eq.count('=') < 1:
        print("The equation must have one = sign.")
        return False
    elif eq.eq.count('=') > 1:
        print("The equation must have one = sign.")
        return False
    return True


def get_cofis(eq):  # Get coeffecents of 'x'
    print(eq.eq)
    if eq.var not in eq.eq:
        return None
    cofis = []
    right_look = True if eq.eq.find(eq.var)+1 != len(eq.eq) else False
    
    if right_look:
        print('looking right')
        if eq.eq[eq.eq.find(eq.var)+1].isdigit():
            print('yes, gitit')
            cofis.append(eq.eq[eq.eq.find(eq.var)+1])

    left_look = True if eq.eq.find(eq.var)+1 != 0 else 1
    if left_look:
        print('looking left')
        if eq.eq[eq.eq.find(eq.var)-1].isdigit():
            cofis.append(eq.eq[eq.eq.find(eq.var)-1])

    return math.prod(cofis) if cofis != [] else [False]

def get_sign(sEq: SubEq):
    pass


def get_x_one_side(eq):
    equation_split = eq.eq.split('=')
    if not eq.var in equation_split[0] or not eq.var in equation_split[1]:
        return eq
    left_cofis = get_cofis(SubEq(equation_split[0], eq.var))
    right_cofis = get_cofis(SubEq(equation_split[1], eq.var))

    print(left_cofis, right_cofis)


if verify(Eq):
    new_equation = get_x_one_side(Eq)
    print(new_equation)
else:
    exit(1)
