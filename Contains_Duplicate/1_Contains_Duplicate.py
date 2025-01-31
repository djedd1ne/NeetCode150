class Solution(object):        
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype bool
        """

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False

"""" Uncomment to test
sol = Solution()
nums = [1, 2, 4, 3, 4]
result = sol.containsDuplicate(nums)
print("Contains duplicate:", result)
"""