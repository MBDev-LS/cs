
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


with open('/Users/louisstevens/Documents/cs/general-programming-practice/Anki Code/marked_cards.json', 'rt') as f: # 
	cardInfoList = json.loads(f.read())


for cardDict in cardInfoList['result']:

	properties = {
		"Note ID": {
			"title": [
				{
					"text": {
						"content": str(cardDict['cardId'])
					}
				}
			]
		},
		"Card Type": {
			"select": {"name": cardDict['modelName']}
		},
		"New Front": {
			"rich_text": [
					{
						"type": "text",
						"text": {
							"content": ""
						}
					}
				]
		},
		"New Back": {
			"rich_text": [
					{
						"type": "text",
						"text": {
							"content": ""
						}
					}
				]
		},
		"Old Front": {
			"rich_text": [
					{
						"type": "text",
						"text": {
							"content": cardDict['fields']['Front']['value'] if cardDict['modelName'] != 'Cloze' else cardDict['fields']['Text']['value']
						}
					}
				]
		},
		"Old Back": {
			"rich_text": [
					{
						"type": "text",
						"text": {
							"content": cardDict['fields']['Back']['value'] if cardDict['modelName'] != 'Cloze' else 'N/A'
						}
					}
				]
		},
	}


	print(properties)

	notion.pages.create(
			parent= {
				"database_id": "e50990ad5c0d4709af0ea1943d925a17"
			},
			properties=properties
		)

# https://www.notion.so/mbls/e50990ad5c0d4709af0ea1943d925a17?v=568b29f85db04d47aa69988929e534c9