class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join([char for char in s if char.isalnum()]) #remove non alphabet chars
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                return False
        return True


            
        