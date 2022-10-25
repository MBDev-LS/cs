
from infix_to_postfix import infix_to_rpn

def main() -> None:
	print('Welcome to the Boolean Algebra Calculator.')
	booleanExpr = input('Enter a boolean expression: ')

	postfixBoolExpr = infix_to_rpn(booleanExpr)

	



if __name__ == '__main__':
	main()