class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[-1]*n
        st=[]
        for i in range(n*2-1,-1,-1):
            while(st and st[-1]<=nums[i%n]):
                st.pop()
            if i<n:
                if st:
                    result[i]=st[-1]
            st.append(nums[i%n])
        return result