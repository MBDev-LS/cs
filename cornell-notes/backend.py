import os

def getSubjects():
	path = os.path.join(os.getcwd(),"cornell-notes","notes")
	directoryContents = os.listdir(path)

	return directoryContents

print(getSubjects())

def getTopics(subject):
	pass

def loadTopic(subject,topic):
	pass