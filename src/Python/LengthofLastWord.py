# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordsArray = s.split()
        lastWordLength = len(wordsArray[-1])
        return lastWordLength

x = Solution()
print(x.lengthOfLastWord("   fly me   to   the moon  "))
