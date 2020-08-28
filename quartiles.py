"""Calculate quartiles without numpy.

    Input:  N (number of scores)
            scores(list of scores)
    Output: print 1st, 2nd, 3rd quartile.
"""

N = int(input())
scores = list(map(int, input().rstrip().split()))
sorted_scores = sorted(scores)

def find_median(scores, N):
    if N % 2 == 1: 
        median = scores[(N//2)]
    else:
        median = (
            (scores[N//2 - 1] + scores[N//2]) / 2 ) 
    print(int(median) )

half_N = int(N//2)  
lower_scores = sorted_scores[0:half_N]
if N%2 == 0:
    upper_scores = sorted_scores[half_N:]
else:
    upper_scores = sorted_scores[half_N + 1:]

find_median(lower_scores, half_N)  
find_median(sorted_scores, N)
find_median(upper_scores, half_N)


# Test case 1

# 7
# 234 -432 0 222 493 -90 2920
# Ans: -90, 222, 224

# Test Case 2
# 10
# 3 7 8 5 12 14 21 15 18 14
# Ans: 7, 13, 15


# Test Case 3
# 9
# 3 7 8 5 12 14 21 13 18
# Ans: 6, 12, 16

# Test Case 4
# 12
# 4 17 7 14 18 12 3 16 10 4 4 12
# Ans: 4, 11, 15






