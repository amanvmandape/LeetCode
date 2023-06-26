class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Efficient Comparison Method
        # Time Complexity: O(n^2)
        # i = 0
        # while i<len(nums):
        #     j=i+1
        #     while j<len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             j+=1
        #     i+=1

        # Hash Table Method
        # Time Complexity: O(n)
        nums_map = {}
        for idx, item in enumerate(nums):
            if (target-item) in nums_map:
                return [nums_map[target-item], idx]
            else:
                nums_map[item] = idx