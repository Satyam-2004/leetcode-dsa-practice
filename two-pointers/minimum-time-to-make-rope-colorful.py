class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        res = 0
        for j in range(1, len(colors)):
            if colors[i] == colors[j]:
                if neededTime[i] < neededTime[j]:
                    res += neededTime[i]
                    i = j
                else:
                    res += neededTime[j]
            else:
                i = j
        return res