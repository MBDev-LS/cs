
from math import inf
import random
import copy

SUPPORTEDSYSTEMS = ['denary', 'binary','hexadecimal']

def intToInt(num: int):
	return str(num)


def intToBin(num: int):
	return bin(num)[2:]


def intToHex(num: int):
	return hex(num)[2:]


def getQuestion(startSystem: str, endSystem: str, min:int =0, max:int =1000):
	number = random.randint(min, max)

	systemFunctions = {
		'den': intToInt,
		'bin': intToBin,
		'hex': intToHex,
	}

	questionDict = {
		'prompt': systemFunctions[startSystem](number),
		'answer': systemFunctions[endSystem](number)
	}

	return questionDict

def intInput(prompt: str, allowBlank: bool=False) -> str:
	userInput = input(prompt)
	while userInput.isdigit is not True and (not allowBlank and userInput == ''):
		userInput = input(prompt)

	return userInput

def endTest(score: int, questionsAnswered: int):
	print(f'\nThe test has ended, you scored {score}/{questionsAnswered} ({round(score/questionsAnswered*100)}%).')
	exit()

minNum = intInput('Enter a minimum value for test values (>0, leave blank for 0): ', True)
maxNum = intInput('Enter a maximum value for test values (leave blank for 1000): ', True)

minNum = int(minNum) if minNum.isdigit() else 0
maxNum = int(maxNum) if maxNum.isdigit() else 1000

numberOfQuestionsToAnswer = intInput('Enter the number of questions you wish to answer (leave blank for infinite): ', True)
numberOfQuestionsToAnswer = int(maxNum) if numberOfQuestionsToAnswer.isdigit() else inf

score = 0
questionsAnswered = 0

while True:
	conversionStart = random.choice(SUPPORTEDSYSTEMS)
	remainingSupportedSystems = copy.copy(SUPPORTEDSYSTEMS)
	remainingSupportedSystems.remove(conversionStart)

	conversionEnd = random.choice(remainingSupportedSystems)

	questionDict = getQuestion(conversionStart[0:3], conversionEnd[0:3], min=minNum, max=maxNum)

	userAnswer = input(f'Convert the {conversionStart} value \'{questionDict["prompt"]}\' to {conversionEnd} (enter \'e\' to exit): ')
	if userAnswer == 'e':
		endTest(score, questionsAnswered)
	
	if userAnswer.lower() == questionDict['answer'].lower():
		score += 1
	
	questionsAnswered += 1

	if questionsAnswered >= numberOfQuestionsToAnswer:
		endTest(score, questionsAnswered)




# Add score counting, setting of min/max options and end mechanic

questionDict = getQuestion('den', 'hex')
print(questionDict['prompt'])
print(questionDict['answer'])