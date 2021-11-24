import string

OPERATORS = "+-/*^()"


class EquationComponent():
    def __init__(self, component: str, decomposed_sub_equation):
        if component not in decomposed_sub_equation:
            return None

        positions = [x for i, x in enumerate(
            decomposed_sub_equation) if x == component]
        # print(positions, decomposed_sub_equation)


class Equation():
    def __init__(self, equation: str, var: str):

        self.eq = equation
        self.var = var

    def verify(self):
        chars = []
        for c in self.eq:
            if not c.isdigit() and c in string.ascii_lowercase:
                chars.append(c)
        if len(list(set(chars))) > 1:
            print(
                'This program currently only supports equations with one unknown variable')
            return False

        if self.eq.count('=') < 1:
            print("The equation must have one = sign.")
            return False
        elif self.eq.count('=') > 1:
            print("The equation must have only one = sign.")
            return False

        if len(self.eq.split('=')[0]) == 0 or len(self.eq.split('=')[0]) == 0:
            print("The must be at least one character on each side of the '=' sign.")
            return False

        return True

    def decompose(self):
        self.left = self.eq.split('=')[0]
        self.left_decomposed = []
        self.right = self.eq.split('=')[1]
        self.right_decomposed = []

        actual_count = 0

        # Repeated code is a product of early testing, real version will store 'left' and 'right' in a list and iterate through it.
        for i, char in enumerate(self.left):
            if not i < actual_count:

                if char in OPERATORS:
                    self.left_decomposed.append(char)
                elif char.isdigit():
                    num = char
                    c = 1
                    if len(self.left)-1 >= i+c:
                        while True and len(self.left)-1 >= i+c:
                            # print(i+c, self.left)
                            if self.left[i+c].isdigit() or self.left[i+c] == self.var:
                                num += self.left[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.left_decomposed.append(num)
                elif char == self.var:
                    num = char
                    c = 1
                    if len(self.left)-1 >= i+c:
                        while True and len(self.left)-1 >= i+c:
                            # print(i+c, self.left)
                            if self.left[i+c].isdigit() or self.left[i+c] == self.var:
                                num += self.left[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.left_decomposed.append(num)

                actual_count += 1

        actual_count = 0
        for i, char in enumerate(self.right):
            if not i < actual_count:

                if char in OPERATORS:
                    self.right_decomposed.append(char)
                elif char.isdigit():
                    num = char
                    c = 1
                    if len(self.right)-1 >= i+c:
                        while True and len(self.right)-1 >= i+c:
                            # print(i+c, self.right)
                            if self.right[i+c].isdigit() or self.right[i+c] == self.var:
                                num += self.right[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.right_decomposed.append(num)
                elif char == self.var:
                    num = char
                    c = 1
                    if len(self.right)-1 >= i+c:
                        print("working")
                        while True and len(self.right)-1 >= i+c:
                            # print(i+c, self.right)
                            if self.right[i+c].isdigit() or self.right[i+c] == self.var:
                                print("working")
                                num += self.right[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.right_decomposed.append(num)

                actual_count += 1

        return [self.left_decomposed, self.right_decomposed]

        """for i, item in enumerate(self.right_decomposed):
            # subEq = EquationComponent(item, self.right_decomposed)
            print(item)
            if item == '-':
                if self.right_decomposed[i-1].isdigit():
                    continue
                elif self.right_decomposed[i-1] == '-':
                    """

    def __str__(self):
        return self.eq


Eq = Equation("x=1/(2*2)+(2^4+4)/2", 'x')
Eq.verify()
decomosedEq = Eq.decompose()


def lsplit(lst, item):
    try:
        index = lst.index(item)
        return [lst[:index], lst[index+1:]]
    except:
        return [lst, lst]


operators = {'+': 2, '-': 2, '/': 3, '*': 3, '^': 4}
operators_associativity = {'+': 'left', '-': 'left', '/': 'left', '*': 'left', '^': 'right'}
stack = []
output = ''

# print(decomosedEq)

for comp in decomosedEq[1]:
    # print(comp)
    if comp == '(':
        stack.append(comp)
    elif comp == ')':
        if len(stack) == 0:
            continue
        while stack[len(stack)-1] != '(': # Terrible way of doing this, what if there are missmatched brackets?
            # print(stack[len(stack)-1], stack)
            output += stack.pop() + ' '
            print(stack, len(stack)-1)
            if len(stack) == 0:
                print("Mismatching brackets.")
                exit()
        if stack[len(stack)-1] == '(':
            stack.pop()
        

    elif not comp in list(operators.keys()):
        output += comp + ' '
    else:
        if len(lsplit(stack, '(')[1]) > 0 and (operators[stack[len(stack)-1]] > operators[comp] or (operators[stack[len(stack)-1]] == operators[comp] and operators_associativity[comp] == 'left')):
            output += stack.pop() + ' '
        stack.append(comp)


stack.reverse()

for comp in stack:
    if comp != '(':
        output += comp + ' '


# output += ''.join([comp for comp in stack if not '('])


print(stack, output)