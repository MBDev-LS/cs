import os

def getSubjects():
	path = os.path.join(os.getcwd(),"cornell-notes","notes")
	directoryContents = os.listdir(path)
	for i in range(len(directoryContents)):
		print(directoryContents[i])

getSubjects()

def getTopics(subject):
	pass

def loadTopic(subject,topic):
	pass