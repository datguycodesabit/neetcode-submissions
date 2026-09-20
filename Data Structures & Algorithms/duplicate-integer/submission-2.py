class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHashSet = set()

        for i in range(len(nums)):
            if nums[i] in numHashSet:
                return True
            numHashSet.add(nums[i])
        return False