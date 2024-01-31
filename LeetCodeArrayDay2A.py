#problem link :https://leetcode.com/problems/minimum-number-game/submissions/1162264247/

#mysolution :

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr =[]
        if len(nums)<=1:
            return nums
        else :

            for i in range(int(len(nums)/2)):
                 #nums = [x for x in nums if x not in arr]
                 alice = min(nums)
                 nums.remove(alice)
                 bob = min(nums)
                 nums.remove(bob)
                 arr.append(bob)
                 arr.append(alice)
            return arr


#optimize solution
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        #This is a sorted array.
        nums=sorted(nums) 
        # Swap each pair via loop
        for i in range(0,len(nums),2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        #Return the final array
        return nums 

        
