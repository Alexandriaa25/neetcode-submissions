class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):
            needed_num = target - n
            if needed_num in seen:
                return [seen[needed_num], i]
            seen[n] = i
        