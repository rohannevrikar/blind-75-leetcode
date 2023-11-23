class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #result would be product of items before and after the current item

        mul = 1
        pre = []
        post = []
        for i in range(len(nums)):
            mul *= nums[i]
            pre.append(mul) #store product of all "before" items
        
        mul = 1

        for j in range(len(nums)-1, -1, -1):
            print(nums[j])
            mul *= nums[j]
            post.append(mul) #store product of all "after" items
        
        post.reverse() # to correspond with current items, or else the first item in post[] would be value of last item of nums

        res = []
        for i in range(len(nums)):
            if(i==0): # there will not be any prefix/postfix of first and last values, hence multiply by 1
                prefix = 1
            else:
                prefix = pre[i-1]
            if(i==len(nums)-1):
                postfix = 1
            else:
                postfix = post[i+1]
            
            res.append(prefix*postfix)
        return res