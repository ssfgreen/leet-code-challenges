"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# Solution
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {}
        for i, val in enumerate(nums):
            remain = target - val
            if remain in val_map:
                return [i, val_map[remain]]
            val_map[val] = i

# Original Solution
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, initial in enumerate(nums):
            remain = target - initial
            for i2, num in enumerate(nums[i+1:]):
                if(num == remain):
                    return [i, i+1+i2]
"""

if(__name__ == "__main__"):
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))