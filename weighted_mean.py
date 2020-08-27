"""Calculate the weighted mean.

   Inputs 
   N: is the number of elements.
   scores: array containing scores.
   weights: array containing weights.

   Output: Weighted mean to 1 decimal.
"""

N = int(input())
scores = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))
total = 0
for i in range(N):
    total = total + (scores[i] * weights[i])

weight = sum(weights)

print("{0:0.1f}".format(total/weight)) 

Test Case 1

5
10 40 30 50 20
1 2 3 4 5

Test Case 2
5
10 -40 30 -50 20
1 2 3 4 5

Test Case 3
5
10 -40 30 50 -20
1 2 3 4 -5