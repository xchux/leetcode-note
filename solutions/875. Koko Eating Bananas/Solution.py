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
