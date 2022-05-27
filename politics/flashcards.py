import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')

party = 'Liberal Democrats'

while True:
    leaderInput = input('Enter the leader\'s name (leave blank for paste): ')
    leaderInput = leaderInput if leaderInput != '' else pyperclip.paste()

    termStartInput = input('Enter the start of the leaders term (leave blank for paste): ')
    termStartInput = termStartInput if termStartInput != '' else pyperclip.paste()

    termEndInput = input('Enter the end of the leaders term (leave blank for paste): ')
    termEndInput = termEndInput if termEndInput != '' else pyperclip.paste()

    pyperclip.copy(f'Who was the leader of the {party} party from {termStartInput} to {termEndInput}?')
    input(f'Copied Q1 ({f"Who was the leader of the {party} party from {termStartInput} to {termEndInput}?"}), press enter to copy A1: ')
    pyperclip.copy(f'{leaderInput} was the leader of the {party} party from {termStartInput} to {termEndInput}.')
    
    input(f'Copied A1 ({f"{leaderInput} was the leader of the {party} party from {termStartInput} to {termEndInput}."}), press enter to copy Q2: ')
    pyperclip.copy(f'During what time period was {leaderInput} leader of the {party} party?')
    input(f'Copied Q2 ({f"During what time period was {leaderInput} leader of the {party} party?"}), press enter to copy A2: ')
    pyperclip.copy(f'{leaderInput} was the leader of the {party} party from {termStartInput} to {termEndInput}.')
    input(f'Copied A2 ({f"{leaderInput} was the leader of the {party} party from {termStartInput} to {termEndInput}."}), press enter to move on to the next leader: ')