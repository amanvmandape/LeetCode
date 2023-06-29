class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        if x<9:
            return True
        
        num_str = ""
        while x>0:
            num_str += str(x%10)
            x = int(x/10)
        
        if num_str == num_str[::-1]:
            return True
        
        '''
        121
        str     x
        1       12
        12      1
        121     0
        '''
        
        