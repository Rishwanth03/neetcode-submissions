class Solution:
    def subsetXORSum(self, nums):
        self.total = 0

        def dfs(index, xor_value):
            # If we've considered all elements
            if index == len(nums):
                self.total += xor_value
                return

            # Don't include current element
            dfs(index + 1, xor_value)

            # Include current element
            dfs(index + 1, xor_value ^ nums[index])

        dfs(0, 0)
        return self.total