class Solution(object):

    def isPossible(self,target,nums,lent):
        currentSum= 0 

        for i in range(lent):
            currentSum= currentSum+nums[i]
        if currentSum >= target:
            return True
        start = 1 
        end = lent

        while end <len(nums):
          currentSum = currentSum - nums[start-1]+nums[end]
          start+=1
          end+=1
          if currentSum >= target:
            return True
        return False   



    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n= len(nums)
        start = 1
        end = n
        ans=0

        while start<=end:
            mid = (start+end)//2
            if self.isPossible(target,nums,mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

