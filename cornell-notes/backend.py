import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
NOTE_DIR = BASE_DIR / 'notes'

def getSubjects():
	try:
		directoryContents = os.listdir(NOTE_DIR)
		return {"success": True, "subjects": directoryContents}
	except FileNotFoundError:
		return {"success": False, "error": "the notes directory cannot be found"}

def getTopics(subject):
	try:
		directoryContents = os.listdir(NOTE_DIR / subject)
		return {"success": True, "topics": [file[:-5] for file in directoryContents]}
	except FileNotFoundError:
		try:
			os.listdir(NOTE_DIR)
		except:
			return {"success": False, "error": "the notes directory cannot be found"}
		else:
			return {"success": False, "error": "this subject does not exist"}

def loadTopic(subject,topic):
	pass

print(getSubjects())
print(getTopics("Subjecet One"))