class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        #number : frequency

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        in_order = sorted(frequencies, key = frequencies.get, reverse=True)

        return in_order[:k]

