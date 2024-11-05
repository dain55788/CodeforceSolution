# Vanya and the cubes
""" Vanya got n cubes. He decided to build a pyramid from them. 
Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, 
the second level must consist of 1 + 2 = 3 cubes, the third level must have 1 + 2 + 3 = 6 cubes, and so on. 
Thus, the i-th level of the pyramid must have 1 + 2 + ... + (i - 1) + i cubes.

Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes. """

n = int(input())
max_height = 0 #i-th level of the pyramid
cube = 0
while cube <= n:
    max_height += 1
    cube += ((max_height*(max_height+1))/2)
print(max_height-1) # -1 because the number of cubes exceeded the given cubes
