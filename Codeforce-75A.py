""" A.Life Without Zeros

Can you imagine our life if we removed all zeros from it? For sure we will have many problems.

In this problem we will have a simple example if we removed all zeros from our life, it's the addition operation. 
Let's assume you are given this equation a + b = c, where a and b are positive integers, and c is the sum of a and b. Now let's remove all zeros from this equation. Will the equation remain correct after removing all zeros?

For example if the equation is 101 + 102 = 203, if we removed all zeros it will be 11 + 12 = 23 which is still a correct equation.

But if the equation is 105 + 106 = 211, if we removed all zeros it will be 15 + 16 = 211 which is not a correct equation. """

a = int(input())
b = int(input())
c = a + b

def remove_zeros(num):
    m = 0
    pow = 1
    while num != 0:
        d = num % 10
        num //= 10
        if d != 0:
            m += d * pow
            pow *= 10
    return m

A = remove_zeros(a)
B = remove_zeros(b)
C = remove_zeros(c)

if A + B == C:
    print("YES")
else:
    print("NO")
