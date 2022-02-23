works = []

for i in range(10000, 10000000):
	digSum = 0
	for dig in str(i):
		digSum += int(dig)**5
	if digSum == i:
		works.append(i)

print(works)
print(len(works))
