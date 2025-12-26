'''QUESTION - Write a recursive function named linear that accepts the following arguments:

P: a non-empty list of positive integers
Q: a non-empty list of positive integers
k: a positive integer
It should return True only if both the conditions given below are satisfied:
P and Q are of same length.
P[i]=k⋅Q[i],or every integer i in the range [0,len(P)-1], endpoints inclusive.
'''

# PLATFORM - IITM Course

def linear(P, Q, k):
  
    if len(P) != len(Q):
        return False
    if len(P) > 1:
        if P[0] != k*Q[0]:
            return False
        else:
            return linear(P[1:],Q[1:],k)
    elif len(P)==1:
        return P[0]==k*Q[0]