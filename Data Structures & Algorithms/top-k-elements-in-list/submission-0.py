class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        gg = Counter(nums)
        ans=[]
        for i in gg.most_common(k):
            item=i[0]
            ans.append(item)
        return ans


        