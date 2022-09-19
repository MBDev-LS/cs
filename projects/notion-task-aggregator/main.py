
from base64 import decodebytes
import config

from pytion import Notion
from pytion.models import Property


no = Notion(token=config.NOTION_SECRET)

# csRevDatabase = no.databases.get(config.DATABASE_ID)  # retrieve database data (not content) and create object

# pages = database.db_filter(property_name="Done", property_type="checkbox", value=False, descending="title")
# pages = csRevDatabase.db_query()

# for page in pages.obj.array:
#     dbBlock = no.pages.get(page.id).get_block_children().obj.array[3]
#     database = no.databases.get(dbBlock.id)
#     print(database.db_query())

def update_cs_task_counts():
	csRevDatabase = no.databases.get(config.DATABASE_ID)
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
			print(f'[LOG ERROR] {len(databasesOnPage)} databases on page, should be exactly 1')
		
		taskListDatabase = databasesOnPage[0]
		taskListDatabasePages = taskListDatabase.db_query()

		numOfTasks = len(taskListDatabasePages.obj.array)
		actualTopicPage = no.pages.get(topicPage.id)
		newProp = Property.create("number") # Do I have to do this?
		actualTopicPage.page_update(topicPage.id, properties={'Tasks': numOfTasks}) # 'int' object has no attribute 'get' - I take it numOfTasks is the 'int' object


update_cs_task_counts()
