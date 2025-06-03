'''
1.imamo int array nums
2.treba vratit array answer tako da je answer[i] = množenju svih elemenata osim answer[i]
3.O(n) time bez dijeljenja


'''
nums = [5,6,7,8]
answer = [1]* len(nums)#1,1,1,1
for i in range (1,len(nums)):
    answer[i] = nums[i-1]*answer[i-1]

print(answer)
right=nums[-1]
for i in range (len(nums)-2,0-1,-1):
    answer[i]*=right
    right*=nums[i]
print(answer)














#nums = [1,2,3,4]
# answer = []
# append = 1
# for i in range(len(nums)):
#     for j in range (len(nums)):
#         if(j != i):
#             append*= nums[j]
    
#     answer.append(append)
#     append = 1

# print(answer)

# nums = [1,2,3,4]
# length = len(nums)
# products = [1] * length #[1,1,1,1]
# for i in range(1, length):
#     products[i] = products[i-1] * nums[i-1]#[1,1,2,6]

# right = nums[-1]#4
# for i in range(length-2, -1, -1):
#     products[i] *= right#[1,1,2,6] pocetno, [1,1,8,6],[1,12,8,6],[24,12,8,6]
#     right *= nums[i]#4*3=12,12*2=24
        

