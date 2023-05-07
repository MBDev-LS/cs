
import requests
import json

class ExternalArticle():
	def __init__(self, title, author) -> None:
		pass

class NYT_Newswire():
	def __init__(self, key) -> None:
		self.key = key

	def add_key_param(self, requestUrl: str) -> str:
		return f'{requestUrl}?api-key={self.key}'
	
	def handle_req_errors(responseObj) -> dict:
		pass
	
	def get_latest(self, source: str='all', section: str='all'):
		requestUrl = f'https://api.nytimes.com/svc/news/v3/content/{source}/{section}.json'
		responseObj = requests.get(self.add_key_param(requestUrl))
		responseDict = json.loads(responseObj.text)

		# Convert to Article()

		return responseDict
	


nw = NYT_Newswire()
