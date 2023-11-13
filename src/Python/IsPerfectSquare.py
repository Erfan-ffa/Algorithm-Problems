import math


class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		if(num == 1):
			return True
		result = False
		remainedNum = num
		while remainedNum > 0:
			remainedNum = int(remainedNum / 2)
			remainedNumPowerTwo = remainedNum * remainedNum
			if(remainedNumPowerTwo == num):
				result = True
				break
			elif(remainedNumPowerTwo < num):
				endNumber = int(remainedNum * 2)
				for i in range(remainedNum, endNumber + 1):
					if((i * i) == num):
						result = True
						break
		return result



s = Solution()
print(s.isPerfectSquare(4))