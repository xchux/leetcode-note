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
