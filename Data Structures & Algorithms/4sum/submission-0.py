class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        result = []

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    for d in range(c+1, len(nums)):

                        total = nums[a] + nums[b] + nums[c] + nums[d]

                        if total == target:
                            quadruplets = [nums[a] , nums[b], nums[c], nums[d]]
                            quadruplets.sort()

                            if quadruplets not in result:
                                result.append(quadruplets)

        return result
        