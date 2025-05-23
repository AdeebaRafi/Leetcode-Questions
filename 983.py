class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)  # Convert list to set for O(1) lookup
        last_day = days[-1]  # Last travel day
        dp = [0] * (last_day + 1)  # DP array from day 0 to last_day

        for i in range(1, last_day + 1):
            if i not in day_set:
                # No travel today, so cost remains same as yesterday
                dp[i] = dp[i - 1]
            else:
                # Travel today, pick minimum of 1-day, 7-day, or 30-day pass
                cost1 = dp[i - 1] + costs[0]                # 1-day pass
                cost7 = dp[max(0, i - 7)] + costs[1]         # 7-day pass
                cost30 = dp[max(0, i - 30)] + costs[2]       # 30-day pass
                dp[i] = min(cost1, cost7, cost30)            # Choose the best

        return dp[last_day]  # Answer is total cost up to last travel day