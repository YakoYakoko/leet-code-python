# 0448_find_all_numbers_disappeared_in_an_array.py

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nume = set(nums)
        conesp = set(range(1, n + 1))
        dif = conesp - nume
        return list(dif)


# --- Pruebas locales ---
if __name__ == "__main__":
    sol = Solution()
    print("Prueba 1:", sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Salida: [5, 6]
    print("Prueba 2:", sol.findDisappearedNumbers([1, 1]))                    # Salida: [2]