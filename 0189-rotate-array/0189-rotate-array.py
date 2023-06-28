class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if(len(nums)>1):
            
            if k>len(nums):
                k = k % len(nums)
                
            shifted = [0]*len(nums)

            for i in range(len(nums)):
                j = i+k
                if j<len(nums):
                    shifted[j] = nums[i]
                else:
                    shifted[j-len(nums)] = nums [i]

            for i in range(len(nums)):
                nums[i] = shifted[i]
            