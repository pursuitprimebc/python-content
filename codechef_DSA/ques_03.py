'''QUESTION - Ticket Fine
On a certain train, Chef-the ticket collector, collects a fine of Rs. X if a passenger is travelling without a ticket. It is known that a passenger carries either a single ticket or no ticket.
P passengers are travelling and they have a total of Q tickets. Help Chef calculate the total fine collected.

Input Format
The first line contains a single integer T, the number of test cases. T lines follow. Each following line contains three integers separated by spaces, whose description follows.

The first integer, X, is the fee in rupees.
The second integer, P, is the number of passengers on the train.
The third integer, Q, is the number of tickets Chef collected.

Output Format
The output must consist of T lines.
The ith line must contain a single integer, the total money(in rupees) collected by Chef corresponding to the ith test case.
'''


t = int(input())
for i in range(t):
    x , p , q = map(int, input().split())
    tickets_required = p - q 
    total_fine = tickets_required*x 
    print(total_fine)

