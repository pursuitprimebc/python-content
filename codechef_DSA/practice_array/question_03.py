''' question - Take discount or Not
There are N items in a shop. You know that the price of the i-th item is Ai
 . Chef wants to buy all the N items.

There is also a discount coupon that costs X rupees and reduces the cost of every item by Y rupees. If the price of an item was initially ≤Y, it becomes free, i.e, costs 0.

Determine whether Chef should buy the discount coupon or not. Chef will buy the discount coupon if and only if the total price he pays after buying the discount coupon is strictly less than the price he pays without buying the discount coupon.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
Each test case consists of two lines of input.
The first line of the test case contains three space-separated integers — N, X, and Y.
The second line contains N space-separated integers — A1,A2 ,…,AN
 .
Output Format
For each test case, output COUPON if Chef should buy the discount coupon, and NO COUPON otherwise.
Each letter of the output may be printed in either lowercase or uppercase. For example, the strings coupon, CouPoN, and COUPON will all be treated as equivalent.
'''


class Solution:
    def check_coupon(self, n, x, y, prices):
       
        cost_without_coupon = sum(prices)
        cost_with_coupon = x
        
        for p in prices:
            cost_with_coupon += max(0, p - y)
        if cost_with_coupon < cost_without_coupon:
            return "COUPON"
        else:
            return "NO COUPON"