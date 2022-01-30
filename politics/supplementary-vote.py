CANDIDATES = ['Mr Tickle', 'PC Plumb', 'Moss', 'Jim']
votes = {}
totalNumberOfVoters = 0

for candidate in CANDIDATES:
    votes[candidate] = {'fp': 0, 'sp': 0}


def SelectCandidate(CANDIDATES, preferanceType):
	prompt = '\n'.join([str(i+1) + ' - ' + CANDIDATES[i] for i in range(0, len(CANDIDATES))])
	print(prompt)

	user_input = input(f"Please enter your {preferanceType} preference: ")
	while user_input not in [str(i+1) for i in range(0, len(CANDIDATES))]:
		user_input = input(f"Please enter your {preferanceType} preference: ")
	
	return CANDIDATES[int(user_input)-1]

# while True:
#     votes[SelectCandidate(CANDIDATES, 'first')]['fp'] += 1
#     votes[SelectCandidate(CANDIDATES, 'second')]['sp'] += 1

#     totalNumberOfVoters += 1

#     endElection = input("Would you like to end the election (y/n): ")
#     while endElection not in ['y', 'n']:
#         endElection = input("Would you like to end the election (y/n): ")
    
#     if endElection == 'y':
#         break

votes = {'Mr Tickle': {'fp': 0, 'sp': 0}, 'PC Plumb': {'fp': 0, 'sp': 0}, 'Moss': {'fp': 0, 'sp': 0}, 'Jim': {'fp': 0, 'sp': 0}}

finalTwo = []

for candidate in votes:
    if votes[candidate]['fp'] > totalNumberOfVoters / 2:
        print(f'{candidate} has won the election with a total of {votes[candidate]["fp"]} first preference votes.')
        exit()
    
    if len(finalTwo) < 2:
        finalTwo.append(votes[candidate])
        continue
    
    if votes[candidate]['fp'] > finalTwo[0]['fp'] or votes[candidate]['fp'] > finalTwo[1]['fp']:
        finalTwo.append(votes[candidate])

print(finalTwo)
