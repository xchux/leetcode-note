---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - String
    - Stack
---

# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

## Description

You are given a string s that consists only of the characters `(`, `)`, `{`, `}`, `[`, and `]`. Your task is to determine whether the string is valid.

A string is considered valid if it meets the following conditions:

1. Every opening bracket has a matching closing bracket of the same type.
2. Brackets must close in the correct order (i.e., the most recently opened bracket must be the first one to close).
3. There should not be any unmatched brackets.


**Example 1:**
```
Input: s = "{}"
Output: true
```

**Example 2:**
```
Input: s = "{]"
Output: false
```


**Constraints:**
`1 <= s.length <= 104`
`s` consists of parentheses only `'()[]{}'`.

## Solution

As known valid combination:
```
mapping = { ')': '(', '}': '{', ']': '[' }
```

Let stack has only open parentheses. When a close parenthesis comes, use it as a key to get valid open parenthesis in the mapping. If mapped parentheses and stack top parenthese sare not valid combination, we should return False.

At last, if stack is empty, we should return True.

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if stack == [] or mapping[char] != stack.pop():
                    return False
        return not stack
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
