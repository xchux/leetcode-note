---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - Array
    - Two Pointers
    - Sorting
---

# [15. 3Sum](https://leetcode.com/problems/3sum/description/)

## Description
You're given an array of integers, `nums`. Your task is to find all unique sets of three numbers \([nums[i], nums[j], nums[k]]\) such that:  

1. The indices \(i\), \(j\), and \(k\) are distinct (\(i \neq j \neq k\)).  
2. The sum of the three numbers is zero: \(nums[i] + nums[j] + nums[k] = 0\).  
3. No duplicate triplets should appear in the result set.  

Return a list of all such triplets.


**Example 1:**
```
Input: nums = [[-2, -1, 0, 1, 3]]
Output: [[-1, 0, 1], [-2, -1, 3]]
```

**Example 2:**
```
Input: nums = [[-2, -1, 1, -1, 2, 1]]
Output: [[-1, -1, 2], [-2, 1, 1]]
```


**Constraints:**
`3 <= nums.length <= 3000`
`-10^5 <= nums[i] <= 10^5`

## Solution

Fix a value and use two pointers from bengin and end to loop all combinations sum equal 0.

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int k = 0; k < nums.length - 2; k++) {
            if (k > 0 && nums[k] == nums[k - 1])
                continue;
            int i = k + 1, j = nums.length - 1;
            while (i < j) {
                int sum = nums[k] + nums[i] + nums[j];
                if (sum < 0) {
                    i++;
                } else if (sum > 0) {
                    j--;
                } else {
                    res.add(Arrays.asList(nums[k], nums[i], nums[j]));
                    while (i < j && nums[i] == nums[i + 1])
                        i++;
                    while (i < j && nums[j] == nums[j - 1])
                        j--;
                    i++;
                    j--;
                }
            }
        }
        return res;
    }
}
```

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        returnList = []
        for i, i_num in enumerate(nums):
            if i and i_num == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                sum = i_num + nums[l] + nums[r]
                if sum == 0:
                    returnList.append([i_num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return returnList
```


## Complexity

- Time complexity: $$O(n^2)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

