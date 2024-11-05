# Codeforce 116A: Tram
""" Linear Kingdom has exactly one tram line. It has n stops, numbered from 1 to n in the order of tram's movement. 
At the i-th stop ai passengers exit the tram, while bi passengers enter it. The tram is empty before it arrives at the first stop. 
Also, when the tram arrives at the last stop, all passengers exit so that it becomes empty.

Your task is to calculate the tram's minimum capacity such that the number of people inside the tram at any time never exceeds this capacity. 
!!Note that at each stop all exiting passengers exit before any entering passenger enters the tram. """

"""
Input: n: the number of stops ( 2 <= n <= 1000)
       the following n lines, there are 2 input: ai and bi (the number of passengers that go and enter the tram) (0 <= ai, b_i <= 1000)
Output: the minimum capacity
Ý tưởng: quyết định sử dụng Integer cho bài toán 
Pseudo code:
Input n (the number of stops that we will loop over it)
Input the 2 capacity variables: cur_capa (current capacity) and min_capa(minimum capacities)
Create 2 variable a and b (a: passengers who exit the tram, b: passengers who enter the tram)
iterate over each stops:
    input a, b
    calculate the current number of passengers on the tram: cur_capa = cur_capa - a + b
    whether the current capacity > the minimum capacity:
        ( the current number of passengers exceeds minimum capacity )
        minimum capacity = current capacity
"""
n = int(input())
a = 0 # passengers exit the tram
b = 0 # passengers enter the tram
current_capacity = 0
min_capacity = 0

for i in range(0, n):
    a, b = map(int, input().split())
    current_capacity = current_capacity - a + b
    if current_capacity > min_capacity:
        min_capacity = current_capacity

print(min_capacity)