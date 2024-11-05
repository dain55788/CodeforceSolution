# ELEPHANT STEPS
# https://codeforces.com/contest/617/problem/A
point = int(input())
step = 0

if point % 5 != 0: # try the largest step everytimes
    step += (point//5) + 1
else:
    step += (point//5)
print(step)