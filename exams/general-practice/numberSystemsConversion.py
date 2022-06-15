
from platform import system
import random



def intToInt(num: int):
	return num

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

input('Press enter to begin test: ')

# Add score counting, setting of min/max options and end mechanic

questionDict = getQuestion('den', 'hex')
print(questionDict['prompt'])
print(questionDict['answer'])