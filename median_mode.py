""" Calculate the mean, median, & mode.
"""
import collections

N = int(input())
scores = list(map(int, input().rstrip().split()))

print("{0:0.1f}".format(sum(scores)/N)) # mean
sorted_scores = sorted(scores)

if N % 2 == 1: 
    median = scores[(N//2)]
else:
    median = (
        (sorted_scores[N//2 - 1] + sorted_scores[N//2]) / 2 )  
print("{0:0.1f}".format(median)) # median

# Use counter to count occurences and put in dict.
score_dict = dict((collections.Counter(sorted_scores)))
max_value = max(list(score_dict.values()))

# Find the key corresponding to the max_value value.
mode = [k for k, v in score_dict.items() if v == max_value]
print(min(mode)) # mode

# Test case 1

# 7
# 234 -432 0 222 493 -90 2920

# Test Case 2
# 8
# 20 -20 20 -20 20 -20 20 -20

# Test Case 3
# 10
# -200 -20 20 -20 20 -20 20 -20 77 -90





