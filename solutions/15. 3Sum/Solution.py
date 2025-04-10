class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        returnList = []
        for i, i_num in enumerate(nums):
            if i and i_num == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = i_num + nums[left] + nums[right]
                if sum == 0:
                    returnList.append([i_num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return returnList
