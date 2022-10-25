questions = [
	'Midterm gains: After the midterm elections, the incumbent party holds more seats in the U.S. House of Representatives than after the previous midterm elections.',
	'No primary contest: There is no serious contest for the incumbent party nomination.',
	'Incumbent seeking re-election: The incumbent party candidate is the sitting president.',
	'No third party: There is no significant third party or independent campaign.',
	'Strong short-term economy: The economy is not in recession during the election campaign.',
	'Strong long-term economy: Real per capita economic growth during the term equals or exceeds mean growth during the previous two terms.',
	'Major policy change: The incumbent administration effects major changes in national policy.',
	'No social unrest: There is no sustained social unrest during the term.',
	'No scandal: The incumbent administration is untainted by major scandal.',
	'No foreign/military failure: The incumbent administration suffers no major failure in foreign or military affairs.',
	'Major foreign/military success: The incumbent administration achieves a major success in foreign or military affairs.',
	'Charismatic incumbent: The incumbent party candidate is charismatic or a national hero.',
	'Uncharismatic challenger: The challenging party candidate is not charismatic or a national hero.'
]

def getAnswer(question: str):
	answer = input(question + '\nTrue (t) or False (f):').lower()
	while answer not in ['t', 'f']:
		answer = input(question + '\nTrue (t) or False (f):').lower()
	
	return answer

answers = [getAnswer(question) for question in questions]

if answers.count('f	') >= 6:
	print('Earthquake, incumbent loses.')