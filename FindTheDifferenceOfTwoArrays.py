'''
1. 2 arraya nums1 i nums2
2. trebamo vratit listu answer velicine 2 gdje
 answer[0]: je lista svih posebnih integera u nums1 koji nisu u nums2
 answer[1]: je lista svih posebnih integera u nums2 koji nisu u nums1

'''
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]


#radi ali dosta sporo
# def findDifference(nums1, nums2):
#     answer = [[],[]]
#     answer[0]= {i for i in nums1 if i not in nums2 and i not in answer[0]}
#     answer[1]= {j for j in nums2 if j not in nums1 and j not in answer[1]}
#     answer[0]= list(answer[0])
#     answer[1]=list(answer[1])
#     return(answer)






# print(findDifference(nums1,nums2))

def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2=set(nums2)
    onlyInSet1 = list(set1-set2)
    onlyInSet2 = list(set2-set1)

    return([onlyInSet1,onlyInSet2])






print(findDifference(nums1,nums2))


