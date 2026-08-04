class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a = None
        count = 0
        
        for num in nums:
            if count == 0:
                a = num
            
            if num == a:
                count += 1
            else:
                count -= 1
                
        return a