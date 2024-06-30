from typing import List
"""
    This function finds the indices of two numbers 
    in a list that add up to a target sum.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the 
        two numbers that add up to the target, 
        or an empty list if no such pair exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store seen numbers and their corresponding indices
        map = {}

        # Loop through each element in the list
        for i in range(len(nums)):
            x = nums[i]
            y = target - x

            # Check if the complement has already been seen in the list
            if x in map:
                # If yes, we've found a pair that adds up to the target
                return [i, map[x]]
            else:
                # If not, add the current number and its index to the dictionary
                map[y] = i