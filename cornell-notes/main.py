import backend
import time


def review_cards(topic_name):
	# topic_cards = backend.loadTopic()
	topic_cards = [
		{"meta_data": {"last_reviewed": 1, "next_review": 2, },
			"answer": "A1", "question": "Q1"},
		{"meta_data": {"last_reviewed": 1, "next_review": 2, },
			"answer": "A2", "question": "Q2"},
		{"meta_data": {"last_reviewed": 1, "next_review": 2, },
			"answer": "A3", "question": "Q3"},
		{"meta_data": {"last_reviewed": 1, "next_review": 2, },
			"answer": "A4", "question": "Q4"}
	]
	print(
		f"You are now reviewing {topic_name}, enter 'q' picking a difficulty to exit the topic.")
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
	print("\nSUBJECT LIST")
	print(''.join('- ' + subject + '\n' for subject in backend.getSubjects()))

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

option_functions = {"List subjects": list_subjects, "List Topics": pass_function, "Review Topic": pass_function, "Quit": quit_function}

while True:
	action = menu(list(option_functions.keys()))
	option_functions[action]()

