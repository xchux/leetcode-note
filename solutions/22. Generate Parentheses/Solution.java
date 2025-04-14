import java.util.*;

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