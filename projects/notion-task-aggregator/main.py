
from pprint import pprint
import config
from notion_client import Client


notion = Client(auth=config.NOTION_SECRET)

list_users_response = notion.users.list()
pprint(list_users_response)

# Docs for DBs: https://ramnes.github.io/notion-sdk-py/reference/api_endpoints/#notion_client.api_endpoints.DatabasesEndpoint