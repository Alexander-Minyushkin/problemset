class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        return ( num[ len(num)/2 ])


x = Solution()

print x.majorityElement([1,2,3,9,8,7,2,2,2,2,2,2,2,2,2])

