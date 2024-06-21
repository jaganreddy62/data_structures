#problem link
#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

#solution

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[]
        for i in points:
            x.append(i[0])
        x.sort(reverse=True)
        a=[]
        for i in range(1,len(x)):
            a.append(x[i-1]-x[i])
        return max(a)

        
