
import pyperclip

output = ''

mps = """""".split('\n')

print(mps)

for mpOverview in mps:
	mpName = mpOverview.split(' (')[0]
	mpCon = mpOverview.split(' (')[1][:-1]

	output += f'{mpName}	{mpCon}\n'


pyperclip.copy(output)
print(output)

