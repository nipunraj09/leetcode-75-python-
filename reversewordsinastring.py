class Solution:
    def reverseWords(self, s: str) -> str:
        l= s.split()
        l.reverse()
        x=' '.join(l)
        return x
