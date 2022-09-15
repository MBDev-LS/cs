
import re

EMAIL_REGEX = r'[a-zA-Z0-9]{1,64}@[a-zA-Z0-9]+(\.[a-zA-Z0-9])+'

def checkEmail(emailText):
	return re.match(EMAIL_REGEX, emailText) is not None

emailInput = input('Enter an email: ')
while checkEmail(emailInput) != True:
	print('You fool, only supposed to enter a bloody email address.')

	emailInput = input('Enter an email: ')

print('Well done, you have passed the test and have entered an email address for no reason whatsoever. Have a (moderately) good day.')
