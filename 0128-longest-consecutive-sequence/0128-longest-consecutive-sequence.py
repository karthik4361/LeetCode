class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        finalSet = set()
        for num in nums:
            finalSet.add(num)
        ans = 0
        for num in finalSet:
            if num-1 not in finalSet:
                chain = 1
                while num+1 in finalSet:
                    num += 1
                    chain +=1
                ans = max(ans,chain)
        return ans

                