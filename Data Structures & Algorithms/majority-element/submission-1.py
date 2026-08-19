class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1

        for key in count:
            if count[key] > len(nums)//2:
                return key
        
        #nums.sort
        #return nums[len(nums)//2]