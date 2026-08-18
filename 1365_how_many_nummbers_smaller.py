# 1365_how_many_numbers_smaller.py

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lista = sorted(nums)
        respuesta = {}
        for i, val in enumerate(lista):
            if val not in respuesta:
                respuesta[val] = i
        return [respuesta[x] for x in nums]


# --- Pruebas locales ---
if __name__ == "__main__":
    sol = Solution()
    print("Prueba 1:", sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]
    print("Prueba 2:", sol.smallerNumbersThanCurrent([6, 5, 4, 8]))        # [2, 1, 0, 3]
    print("Prueba 3:", sol.smallerNumbersThanCurrent([7, 7, 7, 7]))        # [0, 0, 0, 0]