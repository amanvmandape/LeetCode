class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewel_map = {}
        
        for jewel in jewels:
            jewel_map[jewel] = 0
        
        for stone in stones:
            if stone in jewel_map:
                jewel_map[stone] += 1
        
        return sum(jewel_map.values())
        