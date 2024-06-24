"""
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.

Example:

Input: arr = {-2,-3,4,-1,-2,1,5,-3}
Output: 7
Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.

Input: arr = {2}
Output: 2
Explanation: The subarray {2} has the largest sum 1.
"""


import time
#brute-force
#time Complexity : O(n**2)
#space Complexity : O(1)
def maxSubArrayBruteForce(arr):
    maxSubSum=float('-inf')
    for i in range(len(arr)):
        maxSub = 0
        for j in range(i,len(arr)):
            maxSub += arr[j]
            if maxSub>maxSubSum:
                maxSubSum = maxSub

    return maxSubSum

#dynamic programming
#time complexity :O(n),space Complexity : O(n)
def maxSubArrayDPP(arr):
    max_sub_array = [0]*len(arr)
    max_sub_array[0] = arr[0]
    for i in range(1,len(arr)):
        if max_sub_array[i-1]>0:
            max_sub_array[i]= max_sub_array[i-1]+arr[i]
        else:
            max_sub_array[i] = arr[i]
    max_sum = float('-inf')
    for i in max_sub_array:
        max_sum = max(max_sum,i)
    return max_sum

#Kadane's Algorithm
#time Complexity : O(n),space Complexity :O(1)
def maxSubArrayKDNA(arr):
    n = len(arr)
    maxSum = -1e8
    currSum = 0

    for i in range(0, n):
        currSum = currSum + arr[i]
        if (currSum > maxSum):
            maxSum = currSum
        if (currSum < 0):
            currSum = 0

    return maxSum


if __name__=='__main__':
    arr = [-2,-3,4,-1,-2,1,5,-3,1,23,42,533,56,35,24,-70]
    start_time = time.time()
    bfr= maxSubArrayBruteForce(arr)
    print('time taken by brute force algorithm {} ,result :{}'.format(time.time()-start_time,bfr))
    start_time = time.time()
    dpr = maxSubArrayDPP(arr)
    print('time taken by  DPP algorithm {} ,result :{}'.format(time.time() - start_time, dpr))
    start_time = time.time()
    kdr = maxSubArrayKDNA(arr)
    print('time taken by Kadanes algorithm {} ,result :{}'.format(time.time() - start_time, kdr))






