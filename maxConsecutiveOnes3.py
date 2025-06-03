'''
1.dan je array nums i int k 
2. treba vratit maksimalni broj jedinica koje idu jedna za drugom ako možemo pretvoriti 0 u jedinicu k puta

'''



# def longestOnes(nums,k):
#     currentOnes = 0
#     maxOnes = 0
#     temp = k
#     for i in range(len(nums)):
#         if(nums[i]==1):
#             currentOnes+=1
#         elif(k!=0):
#             currentOnes+=1
#             k-=1
            
#         else:
            
#             k= temp-1
#             currentOnes=1
#         maxOnes = max(maxOnes,currentOnes)
            
            
#     return maxOnes
            


# def longestOnes(nums,k):
#     #trebamo oduzimat k za svaku 0 i kad je k 0 trebamo se vratit orginalnih k mjesta unazad i vratit k
#     i = 0
#     curOnes=0
#     maxOnes=0
#     temp = k
#     while i < len(nums):
#         if (nums[i]==1):
#             curOnes+=1
#             i+=1
#         elif(k!=0):
#             curOnes+=1
#             k-=1
#             i+=1
#         else:
#             k=temp
#             i-=k
#             curOnes=0
#         maxOnes = max(maxOnes,curOnes)
        
#     return maxOnes





# def longestOnes(nums,k):
#     #idemo putem dok ne naletimo na previse nula, kada naletimo na previse nula krenemo od prve 0 na koju smo naletjeli plus 1
#     #pre sporo
#     i = 0
#     curOnes = 0
#     maxOnes=0
#     temp = k
#     firstZero = 0
#     flag= 0
#     while i<len(nums):
#         if(nums[i]==1):
#             curOnes+=1
#         elif(k==temp and temp != 0):
#             flag=1
#             firstZero = i
#             k-=1
#             curOnes+=1
#         elif(k>0):
#             k-=1
#             curOnes+=1
#         else:
#             if (flag):
#                 i=firstZero
#             k=temp
#             curOnes=0
#         i+=1
#         maxOnes=max(maxOnes,curOnes)
#     return maxOnes



nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3





def longestOnes(nums,k):
    left = MaxOnes = Zeroes = 0
    for right in range(len(nums)):
        if (nums[right]==0):
            Zeroes +=1
        while (Zeroes>k):
            if(nums[left]==0):
                Zeroes-=1
            left+=1
        MaxOnes=max(MaxOnes, right-left+1)
    return MaxOnes

print(longestOnes(nums,k))