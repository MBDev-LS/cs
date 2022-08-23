
import pyperclip

while True:
    userInput = input('Enter: ').replace(' ', '').replace('(', '').replace(')', '')

    numList = userInput.split('-')

    try:
        numList = [int(num) for num in numList]
    except:
        print('Failed to process nums, input invalid.')
        continue
    
    numsSum = sum(numList)

    print(round((sum(numList)/2)*(1/3), 1))
    pyperclip.copy(round((sum(numList)/2)*(1/3), 1))


