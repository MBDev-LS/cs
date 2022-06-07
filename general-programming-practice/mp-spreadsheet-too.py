
import pyperclip

output = ''

while True:
	mpOverview = input('Enter MP: ')
	try:
		mpName = mpOverview.split(' (')[0]
		mpCon = mpOverview.split(' (')[1][:-1]

		output += f'{mpName}	{mpCon}\n'
	except:
		break


pyperclip.copy(output)
print(output)

