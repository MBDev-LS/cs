import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
NOTE_DIR = BASE_DIR / 'notes'

def is_injection_path(string_to_check: str):
    if '..' in string_to_check or '~' in string_to_check or '/' in string_to_check or '\\' in string_to_check or ':' in string_to_check:
        return True
    return False

def getSubjects():
    try:
        directoryContents = os.listdir(NOTE_DIR)
        return {"success": True, "subjects": directoryContents}
    except FileNotFoundError:
        return {"success": False, "error": "the notes directory cannot be found"}

def getTopics(subject):
    # if is_injection_path(subject):
    #     return {"success": False, "error": "forbidden characters detected"}
    if subject == '':
        return {"success": False, "error": "no subject provided"}
    try:
        checkPresence = os.listdir(NOTE_DIR)
        if subject in checkPresence:
            directoryContents = os.listdir(NOTE_DIR / subject)
            return {"success": True, "topics": [file[:-5] for file in directoryContents]}
        else:
            return {"success": False, "error": "subject not found"}
    except FileNotFoundError:
        try:
            os.listdir(NOTE_DIR)
        except:
            return {"success": False, "error": "the notes directory cannot be found"}
        else:
            return {"success": False, "error": "this subject does not exist"}


def loadTopic(subject, topic):
    if is_injection_path(subject) or is_injection_path(topic):
        return {"success": False, "error": "forbidden characters detected"}
    try:
        topicFile = topic + '.json'
        with open(NOTE_DIR / subject / topicFile, "rt") as fp:
            loadedJson = json.loads(fp.read())
            return {"success": True, "topic": loadedJson}
    except:
        try:
            os.listdir(NOTE_DIR)
        except:
            return {"success": False, "error": "the notes directory cannot be found"}
        else:
            return {"success": False, "error": "this topic does not exist"}

def loadSubjectCards(subject):
    subjectCards = []
    topicsList = getTopics(subject)
    if not topicsList["success"]:
        return {"success": False, "error": topicsList["error"]}
    for i, fileName in enumerate(topicsList["topics"]):
        loadedTopic = loadTopic(subject,fileName)
        if loadedTopic["success"]:
            subjectCards += loadedTopic["topic"]["cards"]
        else:
            return {"success": False, "error": "unknown program error"}
    return {"success": True, "subject_cards": subjectCards}

def saveCards(subject, topic, cards):
    checkPresence = os.listdir(NOTE_DIR)
    if not subject in checkPresence:
        return {"success": False, "error": "subject not found"}

    directoryContents = os.listdir(NOTE_DIR / subject)
    fileName = topic + '.json'
    if fileName not in directoryContents:
        return {"success": False, "error": f"topic not found in subject '{subject}'"}
    with open(NOTE_DIR / subject / fileName, 'r') as fp:
        file_dict = json.loads(fp.read())
    file_dict["cards"] = cards
    with open(NOTE_DIR / subject / fileName, 'w') as fp:
        fp.write(json.dumps(file_dict))

# print(saveCards("Subject One", "topic", []))