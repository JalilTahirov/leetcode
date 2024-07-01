from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = ''

        for i in range(len(nums)):
            first_number = nums[i]
            if first_number == prev:
                continue
            if len(nums)-1-i < 2:
                return res
            target = 0 - first_number
            left = i+1
            right = len(nums) - 1
            prev1 = ''
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([first_number,  nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif sum > target:
                    right -= 1
                else:
                    left  += 1
            prev = first_number

            return res




res = Solution.threeSum(Solution,[-2,0,0,2,2])

print(res)





        