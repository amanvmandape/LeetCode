class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        ans = [None] * (2*length)
        
        for index, number in enumerate(nums):
            ans[index] = ans[index+length] = number
        
        return ans