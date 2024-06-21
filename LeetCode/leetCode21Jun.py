"""
leet code link : https://leetcode.com/problems/grumpy-bookstore-owner/description/

There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.

Intuition
The problem is to find the maximum satisfaction that can be achieved by making some customers happy. The customers who are already happy do not need to be made happy again. The customers who are not happy can be made happy by making the grumpy ones happy.
The maximum satisfaction is achieved by making the grumpy ones happy for the maximum number of minutes.

Approach
First, calculate the total satisfaction of the happy customers.
Then, calculate the initial unsatisfied customers.
Slide a window of size minutes over the array, and for each window, calculate the maximum satisfaction that can be achieved by making the grumpy ones happy.
Update the maximum satisfaction if the current window's satisfaction is higher.
Finally, return the total satisfaction of the happy customers plus the maximum satisfaction achieved.
Complexity
Time complexity:O(n)
Space complexity:O(1)


"""
class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, minutes: int) -> int:
        n=len(customers)
        satisfied = 0
        for i in range(n):
            if grumpy[i]==0:
                satisfied+=customers[i]
        #sliding window
        unsatisfied=0
        for i in range(minutes):
            if grumpy[i]==1:
                unsatisfied += customers[i]
        max_unsatisfied = unsatisfied
        for i in range(minutes,n):
            if grumpy[i-minutes] ==1:
                unsatisfied -= customers[i-minutes]
            if grumpy[i] ==1:
                unsatisfied += customers[i]
            max_unsatisfied = max(unsatisfied,max_unsatisfied)

        return max_unsatisfied+satisfied

if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    sol = Solution()
    output = sol.maxSatisfied(customers,grumpy,minutes)
    print(output)






