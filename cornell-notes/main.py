import backend
import time
import random
import config

from pprint import pprint

def seconds_to_minutes(value):
	return value / 60

def seconds_to_days(value):
	return value / 86400

def proccess_undergrad_card(card, indication):
	time_reviewed = round(time.time())
	card["meta_data"]["last_reviewed"] = time_reviewed
	card["meta_data"]["next_review"] = time_reviewed + config.undergrad_intervals[int(indication)-1]
	card["meta_data"]["interval"] = config.undergrad_intervals[int(indication)-1]
	return card

def review_cards(topic_cards):
	print("Enter 'q' picking a difficulty to exit the topic.")
	resulting_cards = topic_cards
	random.shuffle(topic_cards)
	# print(', '.join(card["question"] for card in topic_cards))
	for i, card in enumerate(topic_cards):
		print(card)

		if card["meta_data"]["last_reviewed"] != None:
			print("HAS BEEN REVIEWED")
			if time.time() < card["meta_data"]["next_review"]:
				print("SKIPPING")
				continue

		print(card["question"])
		input()
		print(card["answer"])

		user_indication = input("1: Again, 2: Hard, 3: Good, 4: Easy\n")
		while user_indication not in ["1", "2", "3", "4", "q"]:
			user_indication = input("1: Again, 2: Hard, 3: Good, 4: Easy\n")
		
		if user_indication == 'q':
			return topic_cards
		
		# 1 minute, 10 minutes, 1 day, 4 days
		resulting_cards[i] = proccess_undergrad_card(card, user_indication)
		
		print(resulting_cards[i])

	return resulting_cards


def list_subjects():
	subject_dict = backend.getSubjects()

	if subject_dict['success'] == True:
		print("\nSUBJECT LIST")
		print(''.join('- ' + subject + '\n' for subject in subject_dict["subjects"]))
	else:
		print('\nerror: '+ subject_dict["error"] + '\n')

def list_topics():
	subject_to_list = input('Enter the subject that would would like to list of the topics from: ').rstrip()

	topic_dict = backend.getTopics(subject_to_list)

	if topic_dict['success'] == True:
		print(f"\nTOPIC LIST FOR {subject_to_list.upper()}")
		print(''.join('- ' + subject + '\n' for subject in topic_dict["topics"]))
	else:
		print('\nerror: '+ topic_dict["error"] + '\n')

def review_topic():
	subject = input("Enter the subject of the topic you would like to review: ").rstrip()
	print(subject, backend.getSubjects()['subjects'])
	if subject.lower() not in [check_subject.lower() for check_subject in backend.getSubjects()['subjects']]:
		print("Subject not found, you can use the menu to list subjects.")
		return
	
	try:
		subject_file_name_index = [check_subject.lower() for check_subject in backend.getSubjects()['subjects']].index(subject.lower())
		subject_file_name = backend.getSubjects()['subjects'][subject_file_name_index]
	except:
		print("error: unknown program error (code: rt01)")
	
	topic = input(f"Enter the topic in {subject_file_name} you would like to review: ")
	topics_in_subject = backend.getTopics(subject_file_name)
	
	if not topic.lower() in [topic_name.lower() for topic_name in topics_in_subject["topics"]]:
		print(f"Topic not found in {subject_file_name}.")
		return
	
	try:
		topic_file_name_index = [check_topic.lower() for check_topic in topics_in_subject['topics']].index(topic.lower())
		topic_file_name = topics_in_subject['topics'][topic_file_name_index]
	except:
		print("error: unknown program error (code: rt01)")
	
	loadCards = backend.loadTopic(subject_file_name, topic_file_name)

	if not loadCards["success"] is True:
		print(f"error: {loadCards['error']}")
	
	newCardList = review_cards(loadCards["topic"]["cards"])
	print(newCardList)
	backend.saveCards(subject_file_name, topic_file_name, newCardList)

def review_subject():
	subject = input("Enter the subject of the topic you would like to study: ").rstrip()

	if subject.lower() not in [check_subject.lower() for check_subject in backend.getSubjects()['subjects']]:
		print("Subject not found, you can use the menu to list subjects.")
		return
	
	try:
		subject_file_name_index = [check_subject.lower() for check_subject in backend.getSubjects()['subjects']].index(subject.lower())
		subject_file_name = backend.getSubjects()['subjects'][subject_file_name_index]
	except:
		print("error: unknown program error (code: rt01)")

	load_result = backend.loadSubjectCards(subject_file_name)

	if not load_result["success"]:
		print("error: " + load_result["error"])
	


	newCardList = review_cards(load_result["subject_cards"])
	
	list_of_topics = []
	for card in newCardList:
		new_card = True
		for i, topic_cards in enumerate(list_of_topics):
			if card["meta_data"]["topic"] == topic_cards[0]["meta_data"]["topic"]:
				list_of_topics[i].append(card)
				new_card = False
		if new_card:
			list_of_topics.append([card])
	
	for topic_cards in list_of_topics:
		print(topic_cards, len(list_of_topics))
		print(backend.saveCards(subject_file_name, topic_cards[0]["meta_data"]["topic"], topic_cards))



def quit_function():
	print("Exiting.")
	exit()

def pass_function():
	pass


def menu(options):
	prompt = '\n'.join([str(i+1) + ' - ' + options[i] for i in range(0, len(options))])
	print(prompt)

	user_input = input("Enter a valid choice: ")
	while user_input not in [str(i+1) for i in range(0, len(options))]:
		user_input = input("Enter a valid choice: ")
	
	return options[int(user_input)-1]

option_functions = {"List subjects": list_subjects, "List Topics": list_topics, "Review Topic": review_topic, "Review Subject": review_subject, "Quit": quit_function}

while True:
	action = menu(list(option_functions.keys()))
	print()
	option_functions[action]()

