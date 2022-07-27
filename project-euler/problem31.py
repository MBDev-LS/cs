
from math import floor

from numpy import remainder

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

def getCoinCombos(target: int, targetCache: dict=None):
	
	combos = []
	targetCache = {} if targetCache is None else targetCache

	for coin in COINS:
		times = target // coin
		remainder = target - coin

		if times < 1:
			continue

		if remainder == 0:
			combos.append([coin])
			continue

		remainderCombos = getCoinCombos(remainder, targetCache) if remainder not in targetCache else targetCache[remainder]
		targetCache[remainder] = remainderCombos

		for remCombo in remainderCombos:
			combos.append([coin] + remCombo)
	
	return combos

print(getCoinCombos(target))
