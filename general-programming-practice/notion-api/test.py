

from pprint import pprint
import requests

# reqData = {
# 	"parent": {
# 			"database_id": dbId
# 		},
#     "properties": {
#         "Author": {
#             "type": "multi_select",
# 			"multi_select": "gal-dem"
#         },
#         "Going...": {
#             "id": "[{:;",
#             "name": "Going...",
#             "select": {"options": [{"color": "default", "id": "fjse", "name": "No"}]},
#             "type": "select",
#         },
#         "ISBN": {"type": "rich_text", "rich_text": "TEST-ISBN"},
#         "ISBN Link": {
#             "formula": {
#                 "expression": '"https://isbnsearch.org/search?s=" ' '  prop("ISBN")'
#             },
#             "type": "formula",
#         },
#         "Publisher": {
#             "type": "select",
# 			"select": "Walker Books",
#         },
#         "Status": {
#             "type": "select",
# 			"select": "Uknown"
#         },
#         "Title": [{"type": "title", "title": "Test Title"}],
#     }
# }

reqData = {
	"parent": {
			"database_id": "1a9bbe8599834ceb8c96796411b44030"
		},
    "properties": {
        "title": {"text": "TEST-name"},
    }
}


headers = {
	"Authorization": "Bearer secret_5hMiDxsAGbHjDKqqrZmQivc9PhLmSS2rEalwwtNFMb8",
	"Notion-Version": "2021-08-16",
	"Content-Type": "application/json"
}

res = requests.post('https://api.notion.com/v1/pages', data=reqData, headers=headers)
# res = requests.get('https://api.notion.com/v1/databases/1a9bbe8599834ceb8c96796411b44030', headers=headers)

print(res.status_code)
pprint(res.json())
