class Solution:
    # @return a boolean
    def __init__(self):
        self.closeDict = { '(':')' , '[':']' , '{':'}'}
    
    def isValid(self, s):
        if len(s) == 0: return True
        start = s[0]
        if start in self.closeDict:
            end = self.closeDict[start]
        else: return False
 
        count = 0
        for i in range(0, len(s)):
            if s[i] == start: count +=1
            elif s[i] == end: count -=1
  
            if count == 0: break

        if count != 0: return False
        return ( self.isValid(s[1:i]) and self.isValid(s[i+1:]))

x = Solution()

print x.isValid("({})[]") == True
print x.isValid("()") == True
print x.isValid("[[({})]]]") == False


