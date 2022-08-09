
from notion_client import Client
from pprint import pprint

from config import notionSecret, dbId

notion = Client(auth=notionSecret)

db = notion.databases.retrieve(dbId)
pprint(db)

notion.pages.create(
	parent= {
		"database_id": dbId
	},
	properties= {
		"Name": {
			"title": [
				{
					"text": {
						"content": "Tuscan Kale"
					}
				}
			]
		},
		"selectable": {
			"multi_select": [
				{
					"name": "Vegetable"
				},
				{
					"name": "DADDIO"
				}
			]
		}
	}
)