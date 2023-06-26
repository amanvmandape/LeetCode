class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out_nums = []
        count = 0
        for number in nums:
            if number == 0:
                count+=1
            else:
                out_nums.append(number)
        
        i=0
        while i<count:
            out_nums.append(0)
            i+=1

        for i in range(len(nums)):
            nums[i] = out_nums[i]
            i+=1
        