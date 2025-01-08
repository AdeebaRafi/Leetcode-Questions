class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans=nums+nums
        # return ans
        ans=[]
        for i in range(2):#O(2)
            for j in nums:#O(n), n is number of elements in nums
                ans.append(j)
        return ans