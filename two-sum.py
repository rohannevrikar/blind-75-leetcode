class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            diff = target - n

            otherlist = nums[nums.index(n)+1:] #find the current element in 2nd list, where 2nd list starts from curr position till end

            if(diff in otherlist):
                return [nums.index(n), otherlist.index(diff) + nums.index(n) + 1] # index of 2nd element would be index in the 2nd list + curr element index + 1
