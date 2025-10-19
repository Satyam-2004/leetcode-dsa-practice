class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_array = ''.join(sorted(s))
            res[sorted_array].append(s)
        
        return list(res.values())
        