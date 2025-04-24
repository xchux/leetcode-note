---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Array
    - Stack
    - Sorting
    - Monotonic Stack
---

# [853. Car Fleet](https://leetcode.com/problems/car-fleet/description/)

## Description

There are **n** cars, each located at a certain distance from the starting point (mile 0), and all are headed toward a common destination at a specified target mile.

You’re given two integer arrays, `position` and `speed`, both of length **n**:  
- `position[i]` indicates the starting mile of the **i-th** car.  
- `speed[i]` represents its speed in miles per hour.

Cars cannot overtake one another, but a faster car can catch up to a slower one. When this happens, it forms a **car fleet**, where all cars move together at the speed of the slowest car in that group.

If a car reaches the target at the same time as a fleet, it joins that fleet, even if it arrives exactly at the destination.

Return the **total number of car fleets** that will arrive at the destination.

**Example 1:**
```
Input: target = 13, position = [9,8,0,5], speed = [1,3,4,1]
Output: 2
Explanation:
* The cars starting at 9 (speed 1) and 8 (speed 3) become a fleet, meeting each other at 13. The fleet forms at target.
* The car starting at 0 (speed 4) and 5 (speed 1) become a flleet, meeting each other at 13.
```

**Example 2:**
```
Input: target = 11, position = [2], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
```

**Constraints:**

* `n == position.length == speed.length`
* `1 <= n <= 10^5`
*  `0 < target <= 10^6`
* `0 <= position[i] < target`
* All the values of `position` are unique.
* `0 < speed[i] <= 10^6`

## Solution

```java
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Map<Integer, Double> carMap = new TreeMap<>(Collections.reverseOrder());
        for (int i = 0; i < position.length; i++) {
            carMap.put(position[i], (double) (target - position[i]) / speed[i]);
        }
        int result = 0;
        double current = 0;
        for (double time : carMap.values()) {
            if (time > current) {
                current = time;
                result++;
            }
        }
        return result;
    }
}
```

```python
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time_to_reach = [
            float(target - pos) / spd
            for pos, spd in sorted(zip(position, speed), reverse=True)
        ]
        current = result = 0
        for t in time_to_reach:
            if t > current:
                current = t
                result += 1
        return result
```

## Complexity

- Time complexity: $$O(nlogn)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
