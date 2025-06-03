

'''
1.dan nam je array nums i trebamo izracunat pivot index
2. pivot index je index gdje je sum svih brojeva strogo lijevo od indexa jednaka sumi brojeva strogo desno od indexa
3.ako je prvi index onda sum lijevo je 0 a ako je zadnji index onda je sum desno 0
4.treba vratit mjesto najljevijeg pivot index-a
5.ako ne postoji vracamo -1

'''
nums = [1,2,3]

def pivotIndex(nums):
    leftSum=0
    rightSum = sum(nums)-nums[0]
    if(leftSum==rightSum):
        return 0
    for i in range(1,len(nums)):
        leftSum+=nums[i-1]
        rightSum-=nums[i]
        if(leftSum==rightSum):
            return i

    return -1






print(pivotIndex(nums))