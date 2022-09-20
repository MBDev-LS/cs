
from pprint import pprint
import config
from task_sources import update_db_task_counts, get_tasks_for_database

from pytion import Notion

no = Notion(token=config.NOTION_SECRET)


def getFullTaskList(no: Notion):
	mainTaskList = []

	for database in config.DATABASE_IDS:
		currentDatabaseDict = config.DATABASE_IDS[database]
		mainTaskList += get_tasks_for_database(no, currentDatabaseDict['id'], currentDatabaseDict['types_set'])
	
	return mainTaskList

if __name__ == '__main__':
	pprint(getFullTaskList(no))
