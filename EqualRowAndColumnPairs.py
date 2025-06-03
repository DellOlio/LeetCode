'''
1.n * n int matrix
2. vracamo broj parova ri,ci tako da red i stupac su isti
3. smatraju da red i stupac su isti ako imaju isti elemente istim redosljedom

'''

#dosta sporo
# grid =[[13,13],[13,13]]

# def equalPairs(grid):
#     gridRows = grid
#     lenght = len(grid)
#     gridColumns = [[0 for k in range(lenght)] for k in range(lenght)]
#     counter=0
    
#     for i in range(lenght):
#         for j in range(lenght):
#             gridColumns[i][j]=gridRows[j][i]
    
#     gridRows = sorted(gridRows)
#     gridColumns = sorted(gridColumns)
#     for l in range(lenght):
#         for m in range(lenght):
#             if gridRows[l] == gridColumns[m]:
#                 counter+=1
        


#     return counter
grid =[[3,2,1],[1,7,6],[2,7,7]]

def equalPairs(grid):
    
    lenght = len(grid)
    hashmap = dict()
    
    for i in range(lenght):
        temp = []
        # if(str(grid[i]) not in hashmap):
        #     hashmap[str(grid[i])]=1
        # else:
        #     hashmap[str(grid[i])]+=1
        for j in range(lenght):
            temp.append(str(grid[i])[j])
        if(temp not in hashmap):
            hashmap[temp]=1
        else:
            hashmap[temp]+=1
    return int(grid[0])




print(equalPairs(grid))