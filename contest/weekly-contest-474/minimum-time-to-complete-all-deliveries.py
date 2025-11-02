from math import gcd

class Solution:
    def mininumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d[0], d[1]
        r1, r2 = r[0], r[1]
        D = d1 + d2

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        def can(t: int) -> bool:
            if t < D:
                return False
            avail1 = t - (t // r1)
            avail2 = t - (t // r2)
            if avail1 < d1 or avail2 < d2:
                return False
            lc = lcm(r1, r2)
            lost = t // lc
            avail_slots = t - lost
            return avail_slots >= D
        
        low = D
        high = D + max(r1, r2) * max(d1, d2)
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low