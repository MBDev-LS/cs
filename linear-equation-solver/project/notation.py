from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY

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