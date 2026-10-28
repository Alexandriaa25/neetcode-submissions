class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        my_set = set(nums)

        for num in my_set:
            if num - 1 not in my_set:
                current_sequence = 1
                
                while num + current_sequence in my_set:
                    current_sequence += 1
            
                if current_sequence > longest:
                    longest = current_sequence

        return longest