''' QUESTION - Expense List
Chef has made a list for his monthly expenses. The list has N expenses with index 1 to N. The money spent on each expense depends upon the monthly income of Chef.

Chef spends 50% of his total income on the expense with index 1.
The money spent on the ith expense (i>1) is equal to 50% of the amount remaining, after paying for all expenses with indices less than i.
Given that Chef earns 2^X rupees in a month, find the amount he saves after paying for all N expenses.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers N and X — where N denotes the number of expenses and 2^X denotes the monthly income of Chef.
Output Format
For each test case, output on a new line, the amount saved by Chef after paying for all N expenses.
'''


t= int(input())
for i in range(t):
    n,x = map(int, input().split())
   
    income = 2**x 
    while n>0:
        amount_spent = income // 2
        amount_remaining = income - amount_spent
        income = amount_remaining
        n -= 1
        
    print(income)
    
    