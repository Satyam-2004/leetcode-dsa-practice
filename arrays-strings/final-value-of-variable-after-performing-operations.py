class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for i in range(len(operations)):
            if "--" in operations[i] :
                res -= 1
            else:
                res += 1
        return res