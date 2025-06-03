'''
1.dan je array arr 
2. vracamo true ako je broj ponavljanja svih brojeva poseban za svaki broj(recimo [1,2,2,1,1,3] svi su posebni jer je 1 bio 3 put, 2 2 put i 3 1 put)

'''

#hash map - dict

arr = [-3,0,1,-3,1,1,1,-3,10,0]


def uniqueOccurrences(arr):
    hashMap = dict()
    for i in range(len(arr)):
        if arr[i] not in hashMap:
            hashMap[arr[i]]=1
        else:
            hashMap[arr[i]]+=1
    setCheck = set(hashMap.values())
    return len(hashMap.values())==len(setCheck)

    


print(uniqueOccurrences(arr))
