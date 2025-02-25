#Faster Solution of TwoSum.c: Hash Map/Dictionary 
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i

# Test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Expected output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # Expected output: [1, 2]
print(sol.twoSum([3, 3], 6))  # Expected output: [0, 1]
