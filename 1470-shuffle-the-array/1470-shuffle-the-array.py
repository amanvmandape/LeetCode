class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        new_nums = []
        
        for index in range(n):
            new_nums.append(nums[index])
            new_nums.append(nums[n+index])
        
        return new_nums
        