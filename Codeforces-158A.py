""" A. Next Round
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round,
as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n≥k), and you already know their scores. 
Calculate how many participants will advance to the next round """

n, k = map(int, input().split())
scores = list(map(int, input().split()))
contestant = 0
for score in range(0, len(scores)):
    if scores[score] > 0 and scores[score] >= scores[k-1]:
        contestant += 1

print(contestant)

