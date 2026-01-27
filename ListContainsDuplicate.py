
#Problem Return True if the list has duplicate items and False is Not
#LeetCodeProblem-217
# Difficulty - Easy
# Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        compareset=set()
        for i in nums:
            if  i in compareset:
                return True
            compareset.add(i)
        if len(compareset)==len(nums):
            return False


sols=Solution()
print(sols.containsDuplicate([1,2,3,4,5,1]))