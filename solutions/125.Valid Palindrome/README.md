---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - String
    - Two Pointers
---

# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

## Description

A palindrome is a sequence that reads the same forward and backward.

For this problem, a string is considered a palindrome if:

1. All uppercase letters are converted to lowercase.
2. All non-alphanumeric characters (such as spaces, punctuation, and symbols) are removed.
3. The remaining characters form a sequence that reads identically from both directions.

Your task is to check whether a given string meets these conditions and return true if it does, otherwise return false.

**Example 1:**
```
Input: Was it a car or a cat I saw?
Output: true
Explanation: "wasitacaroracatisaw" is a palindrome.
```

**Example 2:**
```
Input: How are you?
Output: false
Explanation: "howareyou" is not a palindrome.
```

**Constraints:**

`1 <= s.length <= 2 * 10^5`

`s consists only of printable ASCII characters.`

## Solution

Intuitively remove non-alphanumeric and change others to lowercase.

```java
class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) return false;
        }
        return true;
    }
}
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
