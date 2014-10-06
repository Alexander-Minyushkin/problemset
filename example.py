

l = "([()])"


closeDict = { '(':')' , '[':']' , '{':'}'}

def isValid(s):
 #print s
 if len(s) == 0: return True
 start = s[0]
 if start in closeDict:
   end = closeDict[start]
 else: return False
 
 count = 0
 for i in range(0, len(s)):
   if s[i] == start: count +=1
   elif s[i] == end: count -=1
  
   if count == 0: break

 if count != 0: return False
 return ( isValid(s[1:i]) and isValid(s[i+1:]))


print isValid("({})[]") == True
print isValid("()") == True
print isValid("[[({})]]]") == False


