""" A. Array

Vitaly has an array of n distinct integers. Vitaly wants to divide this array into three non-empty sets so as the following conditions hold:

1. The product of all numbers in the first set is less than zero (<0).
2. The product of all numbers in the second set is greater than zero (>0).
3. The product of all numbers in the third set is equal to zero.

Each number from the initial array must occur in exactly one set.
Help Vitaly. Divide the given array. """
def print_array(arr):
    for i in range(arr):
        print(i)

n = int(input())
pos = []
neg = []
zero = []

arr = list(map(int, input().split()))
for x in arr:
    if x == 0:
        zero.append(x)
    elif x > 0:
        pos.append(x)
    elif x < 0:
        neg.append(x)

if (len(pos)) == 0:
    pos.append(neg[-1])
    neg.pop()
    pos.append(neg[-1])
    neg.pop()

if (len(neg) % 2 == 0):
    zero.append(neg[-1])
    neg.pop()

print_array(pos)
print_array(neg)
print_array(zero)

