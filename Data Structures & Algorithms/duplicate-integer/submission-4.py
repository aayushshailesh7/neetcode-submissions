class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Seen = set()
        for num in nums:
            if num in Seen:
                return True
            Seen.add(num)
        return False