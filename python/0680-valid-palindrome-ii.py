class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.is_valid_polindrome(s, l+1, r) or self.is_valid_polindrome(s,l,r-1)
        return True

    def is_valid_polindrome(self, s, i, j):
        while i<j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True