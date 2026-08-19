class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        #n = len(nums)
        #result = []
        #for num in nums:
            #if nums.count(num)> n//3:
                #if num not in result:

                    #result.append(num)
        #result.sort()
        #return result
        

#------------------------------------------------------------------
# using counter version

        count = Counter(nums)
        result = []

        for num, freq in count.items():
            if freq > len(nums)//3:
                result.append(num)

        result.sort()
        return result 