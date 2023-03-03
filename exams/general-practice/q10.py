userWord = input("Enter a word: ")
VOWL_LIST = ['a', 'e', 'i', 'o', 'u']

print(f'Result: {[userWord[charIndex] if userWord[charIndex] not in VOWL_LIST else [userWord[charIndex2] for charIndex2 in range(len(userWord)-1, 0, -1) if userWord[charIndex2] in VOWL_LIST][len([char2 for char2 in [char3 for char3 in userWord][:charIndex-1] if char2 in VOWL_LIST])] for charIndex in range(len([char for char in userWord]))]}')
