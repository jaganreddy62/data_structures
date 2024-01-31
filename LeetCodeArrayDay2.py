#problem link :https://leetcode.com/problems/left-and-right-sum-differences/solutions/3230880/python3-prefix-suffix-sum/


#my solution:
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(abs(sum(nums[:i+1])-sum(nums[i:])))
        return res

#diiferentway

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        prefix=0
        suffix=sum(nums)
        for i in nums:
            prefix += i
            res.append(abs(prefix-suffix))
            suffix -= i
        return res
