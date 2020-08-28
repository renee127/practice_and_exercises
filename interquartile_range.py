"""Calculate interquartile array w/o numpy.

    Input:  N (number of scores)
            element (list of scores)
            freq (freq of corresponding element)
    Output: interquartile range to 1 decimal
"""

n = int(input())
element = list(map(int, input().rstrip().split()))
scores = list()
freq = [int(x) for x in input().strip().split()]
for i in range(n):
    for j in range(freq[i]):
        scores.append(element[i])

scores = sorted(scores)
N = len(scores)

def find_median(scores, N):
    if N % 2 == 1: 
        median = scores[(N//2)]
    else:
        median = (
            (scores[N//2 - 1] + scores[N//2]) / 2 ) 
    return int(median)

half_N = int(N//2)  
lower_scores = scores[0:half_N]
if N%2 == 0:
    upper_scores = scores[half_N:]
else:
    upper_scores = scores[half_N + 1:]


q1 = find_median(lower_scores, half_N) 

q3 = find_median(upper_scores, half_N)

interquartile = q3 - q1

print("{0:0.1f}".format(interquartile))



# Test case 1
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5
# Ans: 9.0





