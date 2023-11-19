class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        if(n <= 1):
            return False
        
        for i in range(1, n):
            if(nums[i] == nums[i-1]):
                return True
        return False