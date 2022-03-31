
import sya_in_func
import postFix_to_tree


def expressionToTree(expression: str):
    postFixWithSpaces = sya_in_func.booleanInFixToPostFix(expression)
    tree = postFix_to_tree.postfixToTree(postFixWithSpaces)

    return tree

def main():
    expression = 'A.B.C+A.C+A.C.D+A.C.~D'
    postFixWithSpaces = sya_in_func.booleanInFixToPostFix(expression)
    tree = postFix_to_tree.postfixToTree(postFixWithSpaces)

    print(postFixWithSpaces)
    postFix_to_tree.tempDisplayTree(tree)

if __name__ == '__main__':
    main()