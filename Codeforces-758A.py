n = int(input())
welfare = list(map(int, input().split()))
max_wel = max(welfare)
min_wel = 0

for wel in welfare:
           min_wel += max_wel - wel

print(min_wel)