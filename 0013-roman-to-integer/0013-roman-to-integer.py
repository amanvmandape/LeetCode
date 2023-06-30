class Solution:
    def romanToInt(self, s: str) -> int:
        tab = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = s.upper()
        val = 0
        num = 0
        
        for i in range(len(s)-1, -1, -1):
            
            if tab[s[i]] >= val:
                num += tab[s[i]]
            else:
                num -= tab[s[i]]
            
            val = tab[s[i]]
            
        return num