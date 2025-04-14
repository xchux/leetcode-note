import operator

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
