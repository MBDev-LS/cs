
from pprint import pprint
from pytion.models import PropertyValue
import time

def output_log(logType: str, message: str) -> None:
	print(f'[LOG {logType}] {message}')

def property_to_python(notionProperty): # Should return None if property not set. Dunno if this works for all of them though. (works for number)
	if notionProperty.raw['type'] == 'number':
		try:
			int(notionProperty.raw['number'])
		except:
			output_log('ERROR', 'Failed to int() notion number property, returning None')
			return None
		else:
			return int(notionProperty.raw['number'])
	elif notionProperty.raw['type'] == 'rich_text':
		try:
			notionProperty.raw['rich_text'][0]['text']['content']
		except:
			output_log('ERROR', 'Failed to int() notion number property, returning None')
			return None
		else:
			return notionProperty.raw['rich_text'][0]['text']['content']
	elif notionProperty.raw['type'] == 'checkbox':
		return notionProperty.raw['checkbox']
	elif notionProperty.type == 'formula':
		if notionProperty.raw['formula']['type'] == 'string':
			return notionProperty.raw['formula']['string']
			
		elif notionProperty.raw['formula']['type'] == 'number':
			try:
				int(notionProperty.raw['formula']['number'])
			except:
				output_log('ERROR', 'Failed to int() formula number')
			else:
				return int(notionProperty.raw['formula']['number'])

	elif notionProperty.type == 'title':
		return notionProperty.value.simple
	else:
		return str(notionProperty.raw[notionProperty.raw['type']])


def update_db_task_counts(no, databaseId: str):
	csRevDatabase = no.databases.get(databaseId)
	csRevDatabasePages = csRevDatabase.db_query()

	for topicPage in csRevDatabasePages.obj.array:
		dbBlocks = no.pages.get(topicPage.id).get_block_children().obj

		databasesOnPage = []

		for block in dbBlocks:
			try: # Why not use isinstance() like is shown in the pytion documentation
				database = no.databases.get(block.id)
				databasesOnPage.append(database)
			except:
				print(f'{block} is not a database')
				continue
			else:
				
				print(f'{block} is a database')
		
		if len(databasesOnPage) != 1:
			print(f'[LOG ERROR] {len(databasesOnPage)} databases on page ({topicPage.title.simple}), should be exactly 1')
			continue
		
		taskListDatabase = databasesOnPage[0]
		taskListDatabasePages = taskListDatabase.db_query()

		numOfTasks = len(taskListDatabasePages.obj.array)
		actualTopicPage = no.pages.get(topicPage.id)
		newPropertyValue = PropertyValue.create('number', numOfTasks)

		actualTopicPage.page_update(topicPage.id, properties={'Tasks': newPropertyValue}) # 'int' object has no attribute 'get' - I take it numOfTasks is the 'int' object

def get_tasks_for_database(no, databaseId: str, topicTypes: bool=False):
	csRevDatabase = no.databases.get(databaseId)
	csRevDatabasePages = csRevDatabase.db_query()

	dataBaseTasks = []

	for topicPage in csRevDatabasePages.obj.array:
		dbBlocks = no.pages.get(topicPage.id).get_block_children().obj

		databasesOnPage = []

		for block in dbBlocks:
			try: # Why not use isinstance() like is shown in the pytion documentation
				database = no.databases.get(block.id)
				databasesOnPage.append(database)
			except:
				print(f'{block} is not a database')
				continue
			else:
				
				print(f'{block} is a database')
		
		if len(databasesOnPage) != 1:
			print(f'[LOG ERROR] {len(databasesOnPage)} databases on page ({topicPage.title.simple}), should be exactly 1')
			continue

		
		taskListDatabase = databasesOnPage[0]
		taskListDatabasePages = taskListDatabase.db_query()

		topicTasks = []

		for taskPage in taskListDatabasePages.obj.array:
			newTaskProperties = {name: property_to_python(data) for name, data in taskPage.properties.items()}
			
			newTaskProperties['status'] = newTaskProperties['API-Status']
			del newTaskProperties['API-Status']

			newTask = {
				'source': {'text': f'{csRevDatabase.obj.title.simple}: {taskListDatabase.obj.title.simple}',
							'topic_url': topicPage.url},
				'last_updated': time.time(),
				'topic_type': None if topicTypes is False else {'name': topicPage.properties['Type'].raw['select']['name'],
																'color': topicPage.properties['Type'].raw['select']['color']},
				'properties': newTaskProperties
			}

			topicTasks.append(newTask)

		dataBaseTasks += topicTasks

		pprint(topicTasks)
	
	return dataBaseTasks

