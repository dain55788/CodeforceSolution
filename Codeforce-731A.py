name = str(input())
total_len = 0

# Idea:
# Check the min distance between 2 path (example: from a -> u, check the min distance
# min(when go clockwise, when go counterclockwise)

total_len = min(abs(ord(name[0]) - ord('a')), 26 - abs(ord(name[0]) - ord('a')))

for	i in range(len(name) - 1):
  diff = abs(ord(name[i+1]) - ord(name[i]))
  total_len += min(diff, 26 - diff)

print(total_len)
