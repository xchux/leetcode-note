---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Array
    - Binary Search
---

# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

## Description

Koko loves eating bananas. There are **n** piles of bananas, where the **i-th** pile contains `piles[i]` bananas. The guards are away and will return in **h** hours.

Koko chooses an eating speed of **k** bananas per hour. Each hour, she selects one pile and eats up to **k** bananas from it. If the pile has fewer than **k** bananas, she eats all of them and does nothing else for the rest of that hour.

Koko prefers to eat at the slowest possible speed, but she still wants to finish all the bananas before the guards return.

Return the **minimum integer k** (bananas per hour) that allows her to finish all the bananas within **h** hours.


**Example 1:**
```
Input: piles = [30,11,23,4,20], h = 6
Output: 31
```

**Example 2:**
```
Input: piles = [905306368,905306368,905306368], h = 1000000000
Output: 3
```

**Constraints:**

* `1 <= piles.length <= 10^4`
* `piles.length <= h <= 10^9`
* `1 <= piles[i] <= 10^9`

## Solution


```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min = 1, max = Arrays.stream(piles).max().getAsInt();
        int ans = max;

        while(min <= max){
            int mid = min + (max - min) / 2;
            long hours = 0;
            for(int pile : piles){
                hours += (pile + mid - 1) / mid;
            }
            if(hours <= h){
                max = mid - 1;
                ans = mid;
            }
            else{
                min = mid + 1;
            }
        }
        return ans;
    }
}
```

```python
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_eating_speed, max_eating_speed = 1, max(piles)
        ans = max_eating_speed

        while min_eating_speed <= max_eating_speed:
            mid = min_eating_speed + (max_eating_speed - min_eating_speed) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                max_eating_speed = mid - 1
                ans = mid
            else:
                min_eating_speed = mid + 1
        return ans
```

## Complexity

- Time complexity: $$O(n log m)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

