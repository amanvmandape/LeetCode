import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        
        # Using Hash Tables to Calculate
        comb_map = {}
        
        for numb in nums:
            if not numb in comb_map:
                comb_map[numb] = 1
            
            else:
                comb_map[numb] += 1
        
        count = 0
        for item in comb_map.values():
            if item == 2:
                count += 1
            if item> 2:
                count += int(math.factorial(item)/(2 * math.factorial(item - 2)))
                
        # Using simple nested loops
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count+=1
        
        return count
                
        
        