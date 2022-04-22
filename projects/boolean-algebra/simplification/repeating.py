# def t(s):
#     i = (s+s).find(s, 1, -1)
#     return None if i == -1 else s[:i]

# print(t('abcdabcabc'))


def checkForRepeat(string) -> bool:
    for i in range(len(string)):
        subString = string[i:]
        firstResult = (subString+subString).find(subString, 1, -1)
        result =  False if firstResult == -1 else True

        if result is True:
            return True
    
    return False



inv: 1
identity: 2
ideopoentce: 3
absorbsion: 4

1213121412131231321

tokenDict = {}
currentToken = 0
outputList = ''

# string = '-involution-identity-involution-idempotence-involution-identity-involution-absorption-involution-identity-involution-idempotence-involution-identity-idempotence-involution'
string = '-involution-identity-involution-idempotence-involution-identity-involution-absorption-involution-identity-involution-idempotence-involution-identity-idempotence-involution-idempotence-identity-involution-identity-idempotence-involution-identity-involution'
string = '-involution-identity-involution-idempotence-involution-identity-involution-absorption-involution-identity-involution-idempotence-involution-identity-idempotence-involution-idempotence-identity-involution-identity-idempotence-involution-identity-involution-idempotence-involution-identity-idempotence-involution-idempotence-identity-involution-identity-absorption-involution-identity-involution-idempotence-involution-identity-involution-absorption-involution-identity-involution-idempotence-involution-identity-idempotence-involution-idempotence-identity-involution-identity'

print(checkForRepeat(string))

lst = string.split('-')

for item in lst:
    if item not in tokenDict:
        currentToken += 1
        tokenDict[item] = str(currentToken)
    
    outputList += tokenDict[item]

for char in outputList:
    print(char)
    input()

print('\n'+outputList)