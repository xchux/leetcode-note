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
