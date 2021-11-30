import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
NOTE_DIR = BASE_DIR / 'notes'

def getSubjects():
	directoryContents = os.listdir(NOTE_DIR)
	return directoryContents

def getTopics(subject):
	pass

def loadTopic(subject,topic):
	pass