import java.util.*;

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
