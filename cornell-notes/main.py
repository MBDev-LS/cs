import backend
import time


def review_topic(topic_name):
    # topic_cards = backend.getTopic()
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
    
    



review_topic("topic")
