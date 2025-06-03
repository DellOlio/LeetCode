'''
1.imamo int array nums
2.vracamo true ako postoji i,j,k tako da i<j<k i nums[i]<nums[j]<nums[k] (pozcija)
3.inace false



'''


nums = [5,6,0,8,6]




def a(nums):
    first = float("inf")
    second = float("inf")
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
print(a(nums))









# def increasingTriplet(nums):

#     while len(nums)>2:
#         smallest = min(nums)
#         biggest = max(nums)
        
#         smallest_position=nums.index(smallest)
#         biggest_position=nums.index(biggest)
#         while biggest_position==0 or biggest_position==1:
#             nums.pop(biggest_position)
#             smallest = min(nums)
#             biggest = max(nums)
#             smallest_position=nums.index(smallest)
#             biggest_position=nums.index(biggest)
#             if(len(nums)<3):
#                 return False
#         while smallest_position == len(nums)-1 or smallest_position == len(nums)-2:
#             nums.pop(smallest_position)
#             smallest = min(nums)
#             biggest = max(nums)
#             smallest_position=nums.index(smallest)
#             biggest_position=nums.index(biggest)
#             if(len(nums)<3):
#                 return False           
#         if smallest_position<biggest_position-1:
#             for i in range(smallest_position,biggest_position):
#                 if nums[i]<biggest and nums[i]>smallest:
#                     return True
#         else:
#             if(biggest_position>len(nums)/2):
#                 nums.pop(smallest_position)
#             else:
#                 nums.pop(biggest_position)
                    
#     return False



# print(increasingTriplet(nums))     




