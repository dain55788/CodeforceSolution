# Domino Piling
""" You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. 
ou are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions. """

m, n = map(int, input().split()) # m x n square
num_domino = (m*n)//2 # maximum num of domino
# 2: the size of the domino
print(num_domino)

