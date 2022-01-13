import re
fl = open("map", "r")
arr = fl.readlines()
lexical = []
atoi = "".join(filter(str.isdigit,arr[0]))
strr = re.sub("\d", "", arr[0])
lexical.append(atoi)
arr_str = [i for i in strr]
lexical = lexical + arr_str
lexical.pop()
arr.pop(0)
arr = list(map(lambda x : x.split("\n")[0] ,arr))
matrix = []

for i in arr:
    oned = []
    for j in i:
        if j == lexical[2]:
            oned.append(0)
        elif j == lexical[1]:
            oned.append(1)
    matrix.append(oned)

def find_max_sub_square(matrix):
    lenRow = len(matrix)
    lenCol = len(matrix[0])
    subMatrix = [[0 for k in range(lenCol)] for l in range(lenRow)]
    fillcoord = []
    for i in range(lenRow):
        for j in range(lenCol):
            if(matrix[i][j] == 1):
                subMatrix[i][j] = min(subMatrix[i][j-1],subMatrix[i-1][j],subMatrix[i-1][j-1]) + 1
            else:
                subMatrix[i][j] = 0

    maxOfSubMatrix = subMatrix[0][0]
    max_i = 0
    max_j =0
    for i in range(lenRow):
        for j in range(lenCol):
            if (maxOfSubMatrix < subMatrix[i][j]):
                maxOfSubMatrix = subMatrix[i][j]
                max_i = i
                max_j = j
    for i in range(max_i, max_i - maxOfSubMatrix , -1):
        for j in range(max_j, max_j - maxOfSubMatrix , -1):
            fillcoord.append((i,j))
    return(fillcoord)

def print_sol(arr,fillcoord):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i,j) in fillcoord:
                print(lexical[3],end="")
            else:
                print(arr[i][j],end="")
        print("")

print_sol(arr, find_max_sub_square(matrix))

#print(find_max_sub_square(matrix))
#print(matrix)
#print(find_max_sub_square(matrix))
