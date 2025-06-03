class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        maxWealth=0
        m=len(accounts)
        n=len(accounts[0])
        for i in range(m):
            wealth=0
            for j in range(n):
                wealth+=accounts[i][j]
            maxWealth=max(maxWealth,wealth)
        return maxWealth