class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Val = set()
        for num in nums:
            if num in Val:
                return True
            Val.add(num)
        return False
        