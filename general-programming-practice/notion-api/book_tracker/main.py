
import copy
import enum
import json


from notion_client import Client
from olclient import OpenLibrary
import isbnlib

from config import notionSecret

ol = OpenLibrary()
notion = Client(auth=notionSecret)

def intInput(prompt: str) -> int:

	userInput = input(prompt)
	while userInput.isdigit() is not True:
		userInput = input(prompt)
	
	return int(userInput)

def selectOption(optionName: str, options: list) -> str:
	outputString = f'\nSelecting {optionName}'
	outputString += ''.join([f'\n{i+1}. {option}' for i, option in enumerate(options)])
	outputString += '\nSelect one: '

	intChoice = intInput(outputString)
	while intChoice < 1 or intChoice > len(options):
		intChoice = intInput(outputString)
	
	return options[intChoice-1]


with open('isbn_list.json', 'rt') as f: # 
	isbnList = json.loads(f.read())["ISBN_List"]


isbnDictList = [{'title': 'The Ruby In The Smoke', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'The Curious Incident Of The Dog In The Night-Time', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Northern Lights', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Journey To The River Sea', 'status': 'Read', 'location': 'Bedroom'}, {'title': 'Ready Player One', 'status': 'Read', 'location': 'Downstairs'}, {'title': "Miss Peregrine's Home For Peculiar Children: The Graphic Novel", 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'Bletchley Park Brainteasers', 'status': 'Not read', 'location': 'Downstairs'}, {'title': "Marvel Rocket & Groot 02: Keep On Truckin'!", 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'Skulduggery Pleasant', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Liccle Bit', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Erebus - The Story Of A Ship', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'The Person Controller', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Boundless', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'The Catcher In The Rye', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'Circus Of Marvels (1) - Circus Of Marvels', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'The Jungle Book', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'The Man Who Planted Trees', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'The Scorch Trials', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Knots And Splices', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'The Secret Of Platform 13', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Stormbreaker - The Graphic Novel', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Point Blanc', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Eagle Strike - The Graphic Novel', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Skeleton Key', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Forgiveness Project - Stories For A Vengeful Age', 'status': 'Not read', 'location': 'Bedroom'}, {'title': 'Stay Where You Are And Then Leave', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'The Complete Chronicles Of Narnia', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'The Complete Chronicles Of Narnia', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': 'We Should All Be Feminists', 'status': 'Not read', 'location': 'Bedroom'}, {'title': 'The Giraffe And The Pelly And Me', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Tales Of Beedle The Bard', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'Harry Potter And The Deathly Hallows', 'status': 'Read', 'location': 'Downstairs'}, {'title': '"I Will Not Be Erased" - Our Stories About Growing Up As People Of Colour', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'The Ha Ha Bonk Book', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Hobbit, Or, There And Back Again', 'status': 'Not read', 'location': 'Downstairs'}, {'title': 'Harry Potter And The Prisoner Of Azkaban', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Harry Potter And The Chamber Of Secrets', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Charlie And The Great Glass Elevator', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Witches', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Fantastic Mr. Fox', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'James And The Giant Peach', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'The Magic Finger', 'status': 'Unknown', 'location': 'Downstairs'}, {'title': "George's Marvellous Medicine", 'status': 'Read', 'location': 'Downstairs'}, {'title': 'Charlie And The Chocolate Factory', 'status': 'Read', 'location': 'Downstairs'}, {'title': 'James And The Giant Peach', 'status': 'Read', 'location': 'Downstairs'}, {'title': "Roald Dahl's Fantabulous Facts: World Book Day", 'status': 'Unknown', 'location': 'Downstairs'}]
newDictList0 = []
for i, isbn in enumerate(isbnList):
	try: 
		# isbnDictList.append(
		# 	{
		# 		"openLibrary": ol.Edition.get(isbn=isbn),
		# 		"isbnlib": isbnlib.meta(isbn)
		# 	}
		# )

		isbnDictList[i]["openLibrary"] = ol.Edition.get(isbn=isbn)
		isbnDictList[i]["isbnlib"] = isbnlib.meta(isbn)
		
		newDictList0.append(copy.deepcopy(isbnDictList[i]))
	except:
		print(f'\nFailed to process ISBN: {isbn}')
	
	print(f' {i+1}/{len(isbnList)} complete. [{"#"*int(100*((i+1)/len(isbnList)))}{"~"*(100-int(100*((i+1)/len(isbnList))))}]', end='\r')

isbnDictList = newDictList0

newIsbnDictList = []
# forStore = []

for isbnDict in isbnDictList:
	print(isbnDict)
	if not 'Title' in isbnDict["isbnlib"].keys() or not 'Authors' in isbnDict["isbnlib"].keys() or not 'ISBN-13' in isbnDict["isbnlib"].keys():
		print("Failed to provide sufficient infomation: ")
		print(isbnDict)
		continue

	print(f'\nProcessed \'{isbnDict["isbnlib"]["Title"]}\'')

	newIsbnDictList.append(copy.deepcopy(isbnDict))

# 	updatedIsbnDict['status'] = selectOption(f'Status', ['Not read', 'Reading', 'Read', 'Unknown'])
# 	updatedIsbnDict['location'] = selectOption(f'Location', ['Bedroom', 'Downstairs', 'No longer owned'])
	
# 	forStore.append({
# 		'title': isbnDict["isbnlib"]["Title"],
# 		'status': updatedIsbnDict['status'],
# 		'location': updatedIsbnDict['location'],
# 	})

# 	newIsbnDictList.append(updatedIsbnDict)

# print(forStore)
isbnDictList = newIsbnDictList

print(isbnDictList)

for isbnDict in isbnDictList:
	openLibraryWork = isbnDict['openLibrary']
	isbnlibWork = isbnDict['isbnlib']
	

	print(f'Processing \'{isbnlibWork["Title"]}\'')
	status = isbnDict['status']
	location = isbnDict['location']

	properties = {
		"Title": {
			"title": [
				{
					"text": {
						"content": f"{isbnlibWork['Title']}"
					}
				}
			]
		},
		"Status": {
			"select": {"name": status}
		},
		"ISBN": {
			"rich_text": [
					{
						"type": "text",
						"text": {
							"content": f"{isbnlibWork['ISBN-13']}"
						}
					}
				]
		},
		"Location": {
			"select": {"name": location}
		},
	}

	authorListToCheck = isbnlibWork['Authors']
	while '' in authorListToCheck:
		authorListToCheck.remove('')

	if len(authorListToCheck) > 0:
		properties["Author"] = {
			"multi_select": [
				{
					"name": f"{author.replace(',', '')}"
				}
			for author in isbnlibWork['Authors']]
		}
	elif len(openLibraryWork.authors) > 0:
		properties["Author"] = {
			"multi_select": [
				{
					"name": f"{author.name.replace(',', '')}"
				}
			for author in openLibraryWork.authors]
		}

	if hasattr(openLibraryWork, 'publishers') is True:
		properties['Publisher'] = {
			"multi_select": [
				{
					"name": f"{author.replace(',', '')}"
				}
			for author in openLibraryWork.publishers]
		}

	print(properties, isbnlibWork, openLibraryWork)

	notion.pages.create(
			parent= {
				"database_id": "1a9bbe8599834ceb8c96796411b44030"
			},
			properties=properties
		)