
import pyperclip

output = ''

mps = """Paul Holmes (Eastleigh)
Alicia Kearns (Rutland and Melton)
Sir Robert Syms (Poole)
Jeremy Wright (Kenilworth and Southam)
Elliot Colburn (Carshalton and Wallington)
Nickie Aiken (Cities of London & Westminster)
Dr Dan Poulter (Central Suffolk and N Ipswich)
Andrew Bridgen (NW Leicestershire)
Tom Tugendhat (Tonbridge & Malling)
Andrea Leadsom (South Northamptonshire)
John Stevenson (Carlisle)""".split('\n')

print(mps)

for mpOverview in mps:
	mpName = mpOverview.split(' (')[0]
	mpCon = mpOverview.split(' (')[1][:-1]

	output += f'{mpName}	{mpCon}\n'


pyperclip.copy(output)
print(output)

