class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for i in nums: #1
            if i in maps:
                maps[i] +=1 
            else:
                maps[i] = 0
        return sorted(maps, key=maps.get,reverse = True)[:k]
        
   
        
