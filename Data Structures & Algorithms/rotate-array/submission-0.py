class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """ for _ in range(k):

            last = nums.pop()
            nums.insert(0,last)
        """
        
        #------------------------------------

        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]