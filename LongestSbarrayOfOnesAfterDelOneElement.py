'''
1. binary array nums
2.brisemo jedan element iz nje
3.vracamo velicinu najduze ne prazne podliste koja sadrzi samo jedinice
4. vracamo 0 ako ne postoji

'''


nums = [1,1,0,1]





def longestSubarray(nums):
    left = 0
    right = 0
    zeros = 1
    for right in range(len(nums)):

        if nums[right]==0:
            zeros-=1
        if zeros<0:
            if(nums[left]==0):
                zeros+=1
            left+=1
    return right-left

print(longestSubarray(nums))