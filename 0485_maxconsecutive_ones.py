class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        actnum = 0 
        maxconsec = 0
        for num in nums: 
            if num == 1:
                actnum += 1
                maxconsec = max(maxconsec, actnum)
            elif num == 0:
                actnum = 0
        return maxconsec

if __name__ == "__main__":
    sol = Solution()
    print("Prueba 1:", sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  
    print("Prueba 2:", sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  