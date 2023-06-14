class Solution(object):
    def permutateHelper(self,idx,ans,nums,visited,ansList):

        if idx==len(nums):
            ansList.append(ans[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i]=1
                ans[idx] = nums[i]
                self.permutateHelper(idx+1,ans,nums,visited,ansList)
                visited[i]=0



    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [0 for i in range(len(nums))]
        visited = [0 for i in range(len(nums))]
        ansList = []
        self.permutateHelper(0,ans,nums,visited,ansList)
        return ansList

