class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        prefix = [0] * n
        prefix[0] = capacity[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + capacity[i]
        
        d = defaultdict(list)
        for r in range(2, n):  # r from 2 to n-1
            d[(capacity[r], prefix[r-1])].append(r)
        
        count = 0
        for l in range(n - 2):  # l from 0 to n-3
            target = prefix[l] + capacity[l]
            key = (capacity[l], target)
            if key in d:
                r_list = d[key]
                idx = bisect.bisect_left(r_list, l + 2)
                count += len(r_list) - idx
        
        return count