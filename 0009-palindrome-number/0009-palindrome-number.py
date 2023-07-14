class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        if x<0:
            return False
        
        elif x<10:
            return True
        
        else:
            pass
        
        y = x
        
        while y != 0:
            digit = y % 10
            y = int(y / 10)
            nums.append(digit)
            
        y = 0
        for index, num in enumerate(nums):
            y += pow(10,(len(nums)-index-1)) * num
        
        if y==x:
            return True
                