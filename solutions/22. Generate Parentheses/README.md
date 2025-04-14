---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - String
    - Dynamic Programming
    - Backtracking
---

# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)

## Description

Given `n` pairs of parentheses, write a function that returns all possible valid combinations of well-formed (i.e., properly opened and closed) parentheses.


**Example 1:**
```
Input: n = 2
Output: ["(())", "()()"]
```

**Example 2:**
```
Input: n = 4
Output: ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
```

**Constraints:**

* `1 <= n <= 8`

## Solution

Require open parentheses before close parentheses. Therefore need to increase number of open parentheses until n at first, then increase number of close parentheses until n.

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        dfs(result, 0, 0, "", n);
        return result;
    }

    public void dfs(List<String> result, int left, int right, String current, int n) {
        if (current.length() == n * 2) {
            result.add(current);
            return;
        }
        if (left < n) {
            dfs(result, left + 1, right, current + "(", n);
        }
        if (right < left) {
            dfs(result, left, right + 1, current + ")", n);
        }
    }
}
```

```python
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
```

## Complexity

- Time complexity: $$O(2^n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
