
from infix_to_postfix import infix_to_rpn
from postfix_to_tree import postfix_to_tree

def main() -> None:
	print('Welcome to the Boolean Algebra Calculator.')
	booleanExpr = input('Enter a boolean expression: ')

	postfixBoolExpr = infix_to_rpn(booleanExpr)
	exprTree = postfix_to_tree(postfixBoolExpr)



if __name__ == '__main__':
	main()