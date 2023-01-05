
# https://youtu.be/UsnRGo4y5FQ

array = [1, 3, 5, 6, 11]
targetSum = 9

def twoSum(array: list, targetSum: int) -> tuple:
	for n1 in array:
		for n2 in array:
			if n1 == n2:
				continue

			if n1 + n2 == targetSum:
				return (n1, n2)

print(twoSum(array, targetSum))
