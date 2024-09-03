class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        count=0
        for num in nums:
            if num in map:
                map[num]=1+map.get(map[num],0)
            else:
                map[num]=1
        result=list(map.items())
        result.sort(reverse=True,key=lambda x : x[1])
        return [i[0] for i in result[0:k]]
