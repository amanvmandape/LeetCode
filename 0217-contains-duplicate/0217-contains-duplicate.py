class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#         pre_num = None
#         nums.sort()
        
#         for num in nums:
#             if num == pre_num:
#                 return True
            
#             pre_num = num

        dict_nums = {}
        
        for num in nums:
            if not num in dict_nums:
                dict_nums[num] = 1
            else:
                return True
            
        return False