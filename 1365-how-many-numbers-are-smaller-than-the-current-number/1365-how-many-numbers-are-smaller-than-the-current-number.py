class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_new = nums.copy()
        nums_new.sort()
        
        count_list = []
        count_map = {}
        
        print(nums_new)
        for index,num in enumerate(nums_new):
            if not num in count_map:
                count_map[num] = index
                
        del nums_new
        
        for num in nums:
            count_list.append(count_map[num])
            
        return count_list