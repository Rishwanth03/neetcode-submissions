class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        word = set()
        left = 0
        max_lenght = 0

        for right in range(len(s)):

            while s[right] in word:
                word.remove(s[left])
                left += 1

            word.add(s[right])

            max_lenght = max(max_lenght , right - left + 1)

        return max_lenght
        