'''
1. dobiamo array nums
2.treba pomainut sve nule na iraj bez da returnamo ista
3.mora se na pravit in place bez iopije arraya

'''





# def moveZeroes(nums):
#     for num in nums:
#         pnt1 = 0
#         pnt2 = 1
#         while pnt2 !=len(nums):
#             if(nums[pnt1]==0):
#                 temp=nums[pnt1]
#                 nums[pnt1]=nums[pnt2]
#                 nums[pnt2]=temp
#             pnt1+=1
            # pnt2+=1
# pre sporo

# def moveZeroes(nums):

#     j = 0
#     for i in range(1,len(nums)):
#         if nums[i] != 0 and nums[j] == 0:
#                 temp=nums[j]
#                 nums[j]=nums[i]
#                 nums[i]=temp
    
#         if nums[j] != 0:
#             j += 1




nums = [0,0,0,1,0,4,5,6]


def moveZeroes(nums):
    j=0
    for i in range(1,len(nums)):
        if(nums[i]!=0 and nums[j]==0):
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
        if nums[j]!=0:
             j+=1     




moveZeroes(nums)
print(nums)
        


