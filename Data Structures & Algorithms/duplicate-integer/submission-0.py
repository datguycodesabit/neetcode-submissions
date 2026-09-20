class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsSorted = sorted(nums)

        for i in range(len(numsSorted) - 1):
            if numsSorted[i] + numsSorted[i+1] == numsSorted[i]*2:
                return True
        
        return False