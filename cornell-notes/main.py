import backend
import time


def review_cards(topic_cards):
	print("Enter 'q' picking a difficulty to exit the topic.")
	for card in topic_cards:
		if not time.time() > card["meta_data"]["next_review"]:
			continue
		print(card["question"])
		input()
		print(card["answer"])
		user_input = input("1: Again, 2: Hard, 3: Good, 4: Easy\n")
		while user_input not in ["1", "2", "3", "4"]:
			user_input = input("1: Again, 2: Hard, 3: Good, 4: Easy\n")
		if user_input == 'q':
			return
		# 1 minute, 10 minutes, 1 day, 4 days
		time_to_wait = [60, 600, 86400, 345600]
		card["next_review"] = round(time.time()) + time_to_wait[int(user_input)-1]
		print(round(time.time()), card["next_review"])


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
	pass

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

option_functions = {"List subjects": list_subjects, "List Topics": list_topics, "Review Topic": pass_function, "Quit": quit_function}

while True:
	action = menu(list(option_functions.keys()))
	option_functions[action]()

