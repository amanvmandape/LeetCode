class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        pre_num = None
        
        nums.sort()
        
        for num in nums:
            if num == pre_num:
                return True
            
            pre_num = num
        
        return False