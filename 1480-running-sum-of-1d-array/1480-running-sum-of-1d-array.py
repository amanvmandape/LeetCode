class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        pre_val = 0
        sums = []
        
        for index, num in enumerate(nums):
            sums.append(num + pre_val)
            pre_val = sums[index]
            
        return sums