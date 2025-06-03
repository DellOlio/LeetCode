'''
1. dan nam je int array nums koji sadrži n elemenata i int k
2.treba vratit najveci average subarraya velicine k


'''
#treba ubrzat
nums = [1,12,-5,-6,50,3]
k = 4
#treba ubrzat
# def findMaxAverage(nums,k):
#     start = 0
#     biggest= ("-inf")
#     while k<len(nums)+1:
#         window = nums[start:k]
#         biggest=max(float(biggest),(sum(window))/(k-start))
#         start+=1
#         k+=1
#     return biggest

# print(findMaxAverage(nums,k))


def findMaxAverage(nums,k):

    currentSum = sum(nums[:k])
    print(nums[:k])
    maxSum = currentSum

    for i in range(k,len(nums)):
        currentSum += nums[i]-nums[i-k]
        maxSum = max(maxSum,currentSum)
    return maxSum/k

print(findMaxAverage(nums,k))