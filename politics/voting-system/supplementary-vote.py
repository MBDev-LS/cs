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

votes = {
    "Shaun BAILEY":
        {
            "party": "Conservative Party Candidate",
            "fp": 893051,
            "sp": 263812
        },
    "Kam BALAYEV":
        {
            "party": "Renew",
            "fp": 7774,
            "sp": 15691
        },
    "Sian BERRY":
        {
            "party": "Green Party",
            "fp": 197976,
            "sp": 486798
        },
    "Count BINFACE":
        {
            "party": "Count Binface for Mayor of London",
            "fp": 24775,
            "sp": 68121
        },
    "Valerie BROWN":
        {
            "party": "The Burning Pink Party",
            "fp": 5305,
            "sp": 11477
        },
    "Piers CORBYN":
        {
            "party": "Let London Live",
            "fp": 20604,
            "sp": 34355
        },
    "Max FOSH":
        {
            "party": "Independent",
            "fp": 6309,
            "sp": 21409
        },
    "Laurence FOX":
        {
            "party": "The Reclaim Party",
            "fp": 47634,
            "sp": 116730
        },
    "Peter John GAMMONS":
        {
            "party": "UKIP",
            "fp": 14393,
            "sp": 72425
        },
    "Richard John Howard HEWISON":
        {
            "party": "Rejoin EU",
            "fp": 28012,
            "sp": 65643
        },
    "Vanessa Helen HUDSON":
        {
            "party": "Animal Welfare Party-People, Animals, Environment",
            "fp": 16826,
            "sp": 63619
        },
    "Steve KELLEHER":
        {
            "party": "Social Democratic Party",
            "fp": 8764,
            "sp": 28836
        },
    "Sadiq Aman KHAN":
        {
            "party": "Labour Party",
            "fp": 1013721,
            "sp": 400478
        },
    "David KURTEN":
        {
            "party": "Heritage Party",
            "fp": 11025,
            "sp": 23043
        },
    "Farah LONDON":
        {
                "party": "Independent",
            "fp": 11869,
            "sp": 46182
        },
    "Nims OBUNGE":
        {
            "party": "Independent",
            "fp": 9682,
            "sp": 20639
        },
    "Niko OMILANA":
        {
            "party": "Independent",
            "fp": 49628,
            "sp": 75199
        },
    "Luisa Manon PORRITT":
        {
            "party": "Liberal Democrats",
            "fp": 111716,
            "sp": 264912
        },
    "Mandu Kate REID":
        {
            "party": "Vote Women's Equality Party on orange",
            "fp": 21182,
            "sp": 83334
        },
    "Brian Benedict ROSE":
        {
            "party": "London Real Party",
                "fp": 31111,
                "sp": 40674
        }
}

totalNumberOfVoters = 2531357 

finalTwo = []

for candidate in votes:
    if votes[candidate]['fp'] > totalNumberOfVoters / 2:
        print(f'{candidate} has won the election with a total of {votes[candidate]["fp"]} first preference votes.')
        exit()
    
    if len(finalTwo) < 2:
        newFrontrunnerDict = votes[candidate]
        newFrontrunnerDict['candidate'] = candidate
        newFrontrunnerDict['total'] = newFrontrunnerDict['fp'] + newFrontrunnerDict['sp']

        finalTwo.append(newFrontrunnerDict)

        continue
    
    if votes[candidate]['fp'] > finalTwo[0]['fp'] or votes[candidate]['fp'] > finalTwo[1]['fp']:
        newFrontrunnerDict = votes[candidate]
        newFrontrunnerDict['candidate'] = candidate
        newFrontrunnerDict['total'] = newFrontrunnerDict['fp'] + newFrontrunnerDict['sp']
        
        finalTwo.append(newFrontrunnerDict)

print

print(sorted(finalTwo, key=lambda k: k['total'])[-1])

winningCandidate = sorted(finalTwo, key=lambda k: k['total'])[-1]

print(f'{winningCandidate["candidate"]} ({winningCandidate["party"]}) won the election with {winningCandidate["fp"]} first preference votes and {winningCandidate["sp"]} second preference votes')
