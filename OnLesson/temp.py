class Solution:

    def numToSumOfHerDigit(n: int):
        return sum(list(map(int, str(n))) * 2)

    def isHappy(self, n: int, allN) -> bool:
        if n == 1:
            return True

        if n in allN:
            return False
        allN.append(n)
        nextN = __class__.numToSumOfHerDigit(n)
        return __class__.isHappy(nextN, allN)

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        allN = []
        allN.append(n)
        nextN = __class__.numToSumOfHerDigit(n)
        return __class__.isHappy(nextN, allN)

    


print(Solution.isHappy(Solution, 12))
