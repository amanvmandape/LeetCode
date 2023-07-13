class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        greatest_candy = max(candies)
        result = []
        
        for candy in candies:
            if (candy + extraCandies) >= greatest_candy:
                result.append(True)
            else:
                result.append(False)
        return result