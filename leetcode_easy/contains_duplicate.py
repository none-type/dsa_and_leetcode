# solution 1 ( big O ?)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(len(nums)):
            if i < len(nums) -1 and nums[i] == nums[i + 1]:
                return True
        return False

# solution 2 (O(n))
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # define hashset store
        hashSet = set()
        # loop through nums
        for num in nums:
            # check if current num in hashset
            if num in hashSet:
                # return True
                return True
            hashSet.add(num)

        # return False
        return False