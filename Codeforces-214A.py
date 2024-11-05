""" 
You are given a system of equations:
{ a**2 + b = n
{ a + b**2 = m
Question: You should count, how many there are pairs of integers (a,b) (0≤a,b) which satisfy the system.

Input
A single line contains two integers n,m (1≤n,m≤1000) — the parameters of the system. The numbers on the line ar e separated by a space.
Output
On a single line print the answer to the problem. 
"""

# Solution: Because a**2 + b = n => It means b = n - a**2 => a + (n - a**2)**2 = m. 
# As we solve a, it means that there is a pair (a, b) that satisfy the system of equations.

import math 

n, m = map(int, input().split())
count = 0
for a in range(0, int(math.sqrt(1000)) + 1):
    if n - pow(a,2) >= 0 and pow(a, 4) + a - (2*pow(a,2)*n) == (-pow(n, 2) + m):
        count += 1
 
print(count)