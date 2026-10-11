class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        smaller_count = {}
        running_total = 0
        for value in sorted(freq):
            smaller_count[value] = running_total
            running_total += freq[value]
        
        return [smaller_count[num] for num in nums]