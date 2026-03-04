#1. # Identifying and removing the duplicates from the list in place 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mine = []  
        for i in nums:
            if i not in mine:   
                mine.append(i)  
        nums[:] = mine  #[:] - refers to the entire contents of the list on the right from start to finish 
        return len(nums)

#2. Given an array of integers and a target number, return the indexes of two numbers that add up to the target number. \
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            residual = target - num
            if residual in numbers:
                return [i, numbers[residual]]
            numbers [num] = i
