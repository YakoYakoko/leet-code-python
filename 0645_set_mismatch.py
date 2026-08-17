# 0645_set_mismatch.py

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lennums = len(nums)
        sumnums = sum(set(nums))
        espsum = sum(range(1, lennums + 1))
        
        dup = sum(nums) - sumnums
        fal = espsum - sumnums
        
        return [dup, fal]


# --- Pruebas locales ---
if __name__ == "__main__":
    sol = Solution()
    print("Prueba 1:", sol.findErrorNums([1, 2, 2, 4]))  # Salida esperada: [2, 3]
    print("Prueba 2:", sol.findErrorNums([1, 1]))        # Salida esperada: [1, 2]