#1. # Identifying and removing the duplicates from the list in place 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mine = []  
        for i in nums:
            if i not in mine:   
                mine.append(i)  
        nums[:] = mine  #[:] - refers to the entire contents of the list on the right from start to finish 
        return len(nums)
