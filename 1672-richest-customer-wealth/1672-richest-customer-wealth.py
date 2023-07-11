class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for cust in accounts:
            total_wealth = sum(cust)
            
            if total_wealth > max_wealth:
                max_wealth = total_wealth
            
        return max_wealth