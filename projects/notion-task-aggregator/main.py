
import config

from pytion import Notion

no = Notion(token=config.NOTION_SECRET)

database = no.databases.get(config.DATABASE_ID)  # retrieve database data (not content) and create object

# retrieve database content by filtering with sorting

# pages = database.db_filter(property_name="Done", property_type="checkbox", value=False, descending="title")
pages = database.db_query()

for page in pages.obj.array:
    dbBlock = no.pages.get(page.id).get_block_children().obj.array[3]
    database = no.databases.get(dbBlock.id)
    print(database.db_query())

