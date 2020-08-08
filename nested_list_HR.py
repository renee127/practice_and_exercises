if __name__ == '__main__':

    nested_list = []
    scores = []
    
    # create a nested list for name/score and 
    # a score list to sort 2nd lowest score
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pair = [] 
        pair.append(name)
        pair.append(score)
        scores.append(score)
        nested_list.append(pair)
    
    # get 2nd lowest score in scores
    scores = set(scores)
    scores = list(scores)
    socres = scores.sort()
    second_lowest_grade = scores[1]
    
    # create list of names with second lowest score
    names = []
    for i in range(len(nested_list)):
        if nested_list[i][1] == second_lowest_grade:
            names.append(nested_list[i][0])

# print out names in alphabetical order
names.sort()
for i in range(len(names)):
    print(names[i])
