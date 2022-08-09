from operator import truediv


with open('input.txt', 'rt') as f:
    readText = f.read()

print(readText.split("'status'")[3])

newText = ''
adding = True

for word in readText:
    print(word)
