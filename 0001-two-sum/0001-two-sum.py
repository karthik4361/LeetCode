class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hset= set()
        ans =[]
        for i in range(len(nums)):
            k = target-nums[i]
            if k in hset:
                ans = [nums.index(k),i]
                break
            hset.add(nums[i])
        return ans 
                
