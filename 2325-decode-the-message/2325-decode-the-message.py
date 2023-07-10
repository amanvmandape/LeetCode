class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        
        hash_tab = {}
        i = 97
        secret_msg = ''
        for char in key:
            if char != ' ' and char not in hash_tab:
                hash_tab[char] = chr(i)
                i+=1
        
        for char in message:
            
            if char == ' ':
                secret_msg += ' '
                
            else:
                secret_msg += hash_tab[char]
        
        return secret_msg