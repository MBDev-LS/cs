
import config
import requests

def sendNotfication(time: str, source: str, content: str):
	requests.post('https://api.mynotifier.app', {
		"apiKey": config.NOTIFY_KEY,
		"message": "London Bridge is down",
		"description": f"Source: {source} at {time}",
		"body": f"The time is {time}, {source} are reporting that: '{content}'",
		"info": "info",
	})
