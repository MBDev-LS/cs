from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY


def lsplit(lst, item):
    try:
        index = lst.index(item)
        return [lst[:index], lst[index+1:]]
    except:
        return [lst, lst]


def infix_to_postfix(Eq):

    decomosedEq = Eq.decompose()
    results = []

    for side in decomosedEq:

        stack = []
        output = ''

        for comp in side:
            if comp == '(':
                stack.append(comp)
            elif comp == ')':
                if len(stack) == 0:
                    continue
                while stack[len(stack)-1] != '(':
                    output += stack.pop() + ' '
                    if len(stack) == 0:
                        print("Mismatching brackets.")
                        exit()
                if stack[len(stack)-1] == '(':
                    stack.pop()

            elif not comp in list(OPERATORS.keys()):
                output += comp + ' '
            else:
                if len(lsplit(stack, '(')[1]) > 0 and (OPERATORS[stack[len(stack)-1]] > OPERATORS[comp] or (OPERATORS[stack[len(stack)-1]] == OPERATORS[comp] and OPERATORS_ASSOCIATIVITY[comp] == 'left')):
                    output += stack.pop() + ' '
                stack.append(comp)

        stack.reverse()

        for comp in stack:
            if comp != '(':
                output += comp + ' '

        results.append(output)

    return results


def eval_postfix(expression: str, var):
    expression = expression.replace(' ', '')

    stack = []

    for comp in expression:
        # print(stack)
        if comp in OPERATORS.keys():
            var_in = False
            operands = [stack.pop(), stack.pop()]

            for i, operand in enumerate(operands):
                if var in operand:
                    print(operand)
                    var_in = True
                    if operand == var:
                        operands[i] = 1
                    else:
                        factors = operand.split(var)
                        print('F', factors)
                        operands[i] = 1

            calc = f"{operands[1]} {comp} {operands[0]}".replace('^', '**')
            # print(calc)
            res = eval(calc)
            stack.append(str(res) + 'x')
        else:
            stack.append(comp)
    # print(stack)
    return stack[0]


print(eval_postfix("1 2 2 * x * 2 * / 2 4 ^ 4 + 2 / + ", 'x'))
