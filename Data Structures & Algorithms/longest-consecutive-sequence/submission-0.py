class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        longest = 0

        for num in num_set:

            # to check if num is start of a sequence

            if num -1 not in num_set:

                lenght = 1

                while num + lenght in num_set:
                    lenght += 1

                longest = max(longest, lenght)

        return longest        

#--------------------------------------------------------------------------------------------
        num_set = set(nums)

        longest = 0
        for num in num_set:

            if num - 1 in num_set:

                lenght = 1
                while num + lenght in num_set:
                    lenght += 1
                
                longest = max(longest , lenght)

        return longest