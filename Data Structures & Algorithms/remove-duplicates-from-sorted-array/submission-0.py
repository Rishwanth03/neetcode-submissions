class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        un = list(set(nums))

        un.sort()

        for i in range(len(un)):
            nums[i] = un[i]
        
        return len(un)
        
        #--------------------------------------

        k = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]:
                nums[k] = num[i]
                k+=1

        return k