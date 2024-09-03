class Solution(object):
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord("a")]+=1
            d[tuple(count)].append(word)
        return d.values()
