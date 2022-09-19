
from pprint import pprint
import config
from notion_client import AsyncClient

notion = AsyncClient(auth=config.NOTION_SECRET)

async def test():
	list_users_response = await notion.users.list()
	pprint(list_users_response)

await test()
