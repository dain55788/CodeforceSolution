# A. Kefa and First Steps
""" Kefa decided to make some money doing business on the Internet for exactly n days. 
He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. 
Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. 
Let us remind you that the subsegment of the sequence is its continuous fragment. 
A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.

Help Kefa cope with this task! """

count_subsegment = 0
n = int(input())
a = list(map(int, input().split()))
max_subsegement = 1

for cur in range(n):
    if a[cur] >= a[cur-1]:
        count_subsegment += 1
        max_subsegement = max(max_subsegement, count_subsegment)
    else:
        count_subsegment = 1

print(max_subsegement)