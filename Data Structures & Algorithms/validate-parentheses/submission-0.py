class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"

        }

        for char in s:
            if char in brackets.values(): #if opening 
                stack.append(char) #add

            else:
                if not stack:
                    return False
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
           
        