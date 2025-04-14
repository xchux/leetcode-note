---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Array
    - Math
    - Stack
---

# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

## Description

An array of strings called `tokens`, which represents an arithmetic expression written in Reverse Polish Notation (RPN).

Your task is to evaluate this expression and return the result as an integer.

Keep in mind:

- Valid operators include `+`, `-`, `*`, and `/`.
- Each operand is either an integer or another valid RPN sub-expression.
- Division between two integers should truncate toward zero.
- You won't need to handle any division by zero.
- The input is guaranteed to form a valid RPN expression.
- Both the final result and all intermediate computations will fit within a 32-bit signed integer.


**Example 1:**
```
Input: tokens = ['3', '2', '+', '2', '*']
Output: 10
Explanation: (3 + 2) * 2 = 10
```

**Example 2:**
```
Input: tokens = ['3', '14', '5', '/', '+']
Output: 5
Explanation: (14 / 5) + 3 = 5
```

**Constraints:**

* `1 <= tokens.length <= 10^4`
* `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.


## Solution

This is a classic postfix expression problem. We use a stack to store operands when encountering numbers, and apply operators by popping values from the stack when an operator is found.

```java
class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                int first = stack.pop();
                int second = stack.pop();
                /* In Java, when using switch with String, the compiler generates code that compares hashCode() first, then uses .equals() for exact match. This makes the average time complexity close to O(1), but the worst-case complexity is O(k), where k is the string length. Therefore, for performance-critical code, using a Map lookup or interning strings for reference comparison can be faster than a switch or chained if-else. */
                if (token.equals("+")) {
                    stack.push(second + first);
                } else if (token.equals("-")) {
                    stack.push(second - first);
                } else if (token.equals("*")) {
                    stack.push(second * first);
                } else if (token.equals("/")) {
                    stack.push(second / first);
                }

            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.peek();
    }
}
```

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        stack = []
        for token in tokens:
            if token in "+-*/":
                first, second = stack.pop(), stack.pop()
                if token != "/":
                    stack.append(ops[token](second, first))
                else:
                    stack.append(int(second / first))
            else:
                stack.append(int(token))
        return stack[0]
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
