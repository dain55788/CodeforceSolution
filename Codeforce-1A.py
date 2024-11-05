# Theatre Square
""" Theatre Square in the capital city of Berland has a rectangular shape with the size n×m meters. On the occasion of the city's anniversary, 
a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a×a.
What is the least number of flagstones needed to pave the Square? 
It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones.
The sides of flagstones should be parallel to the sides of the Square. """

# link: https://codeforces.com/contest/1/problem/A
n, m, a = map(int, input().split())
val1 = 0
val2 = 0
 
if n % a == 0: # if the size a of the fragstone fit into the size n of the square
    val1 += n//a
else:
    val1 = n//a + 1 # if no, need 1 more fragstone because we cannot break the fragstone.
 
if m % a == 0:
    val2 += m//a
else:
    val2 += m//a + 1
 
print((val1 * val2))