---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - Array
    - Two Pointers
    - Binary Search
---

# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Description

You are given a 1-indexed array of integers called numbers, which is already sorted in increasing order.

Your goal is to find two numbers in this array that add up to a given target value. Let’s call their positions index1 and index2, where:

1 <= index1 < index2 <= numbers.length (i.e., index1 comes before index2 in the array).


**Example 1:**
```
Input: numbers = [2, 5, 6], target = 11
Output: [2, 3]
Explanation: The sum of 5 and 6 is 11. Therefore, index1 = 2, index2 = 3. We return [2, 3].
```

**Example 2:**
```
Input: numbers = [1, 2, 5, 6], target = 7
Output: [2, 3]
Explanation: The sum of 2 and 5 is 7. Therefore, index1 = 2, index2 = 3. We return [2, 3].
```


**Constraints:**

`2 <= numbers.length <= 3 * 104`

`-1000 <= numbers[i] <= 1000`

`numbers is sorted in non-decreasing order`

`-1000 <= target <= 1000`

`The tests are generated such that there is exactly one solution.`


## Solution

Initialize two pointers, one at the front and one at the end. Check the sum of the two pointers. If the target is greater than the sum, increase the left pointer; otherwise, decrease the right pointer. Repeat this process until the sum equals the target or the two pointers meet.

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[] {left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return result;
    }
}
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
