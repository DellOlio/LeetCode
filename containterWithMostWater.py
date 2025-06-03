'''
1. dobivamo int array height velicine n.
2.trebamo nac najvecu mogucnost sadrzaja vode tako da je povrsina od (i,0) do (i,height(i))

'''



# def maxArea(height):
    #trebamo nac najvecu povrsinu tako da prvi broj koji uzmemo i height[taj_broj] rade tu najvecu povrsinu
    #gledamo manji broj od ta 2 puta duzina izmedu ta 2
#     helpArray = []
#     for i in range(len(height)):
#         if(height[i]<height[height[i]]):
#             temp = height[i]*(height[i]-i)
#             temp = abs(temp)
#         elif(height[i]>=height[height[i]]):
#             temp = height[height[i]]*(height[i]-i)
#             temp = abs(temp)
#         helpArray.append(temp)
#     print(helpArray)
#     return(max(helpArray))
# print(maxArea(height))


# treba testirati sve linije ne od i do height[i]

height = [1,8,6,2,5,4,8,3,7,6,2]

def maxArea(height):
    #dva pointera

    max_value = 0
    left = 0
    right = len(height)-1
    while left<right:
        max_value = max(max_value,min(height[left],height[right])*(right-left ))
        if (height[left]<height[right]):
            left+=1
        else:
            right-=1
    return max_value
print(maxArea(height))





