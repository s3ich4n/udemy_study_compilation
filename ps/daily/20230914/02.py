class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s.lower()))
        return a == a[::-1]


s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))
