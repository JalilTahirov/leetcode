class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.is_polindrome(w):
                return w
        return ""
    def is_polindrome(self, word:str):
        return word == ''.join(reversed(word))
    


    