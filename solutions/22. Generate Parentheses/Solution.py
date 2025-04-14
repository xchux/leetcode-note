class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.dfs(result, 0, 0, "", n)
        return result
    
    def dfs(self, result: list[str], left: int, right: int, current: str, n: int):
        if left == n and right == n:
            result.append(current)
            return
        if left < n:
            self.dfs(result, left + 1, right, current + "(", n)
        if right < left:
            self.dfs(result, left, right + 1, current + ")", n)
