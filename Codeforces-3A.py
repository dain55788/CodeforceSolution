""" # A. Shortest path of the king

The king is left alone on the chessboard. In spite of this loneliness, he doesn't lose heart, because he has business of national importance.
For example, he has to pay an official visit to square t.
As the king is not in habit of wasting his time, he wants to get from his current position s to square t in the least number of moves. Help him to do this.

"""

def path(s, t): # for example c3, f7
    x = ord(s[0]) - ord(t[0]) # ord('s') - ord('f') = -3
    y = ord(s[1]) - ord(t[1]) # ord(3) - ord(7) = -4
    ans = []
    while x != 0 and y != 0: # if one or 2 == 0 -> stop
        if (x < 0 and y < 0):
            ans.append("RU")
            x += 1
            y += 1
        elif (x > 0 and y > 0):
            x -= 1
            y -= 1
            ans.append("LD")
        elif (x > 0 and y < 0):
            x -= 1
            y += 1
            ans.append("LU")
        elif (x < 0 and y > 0):
            x += 1
            y -= 1
            ans.append("RD")
    while x != 0:
        if x > 0:
            x -= 1
            ans.append("L")
        else:
            x += 1
            ans.append("R")
    while y != 0:
        if y > 0:
            y -= 1
            ans.append("D")
        else:
            y += 1
            ans.append("U")
    return ans
 
s = input()
t = input()
kingPath = path(s, t)
print(len(kingPath))
for path in kingPath:
    print(path)