'''
1. ulaze 2 stringa
2. treba nac koja slova im se podudaraju, da se snjima moze "dijelit"
3.vracamo taj string
'''

str1 = input("str1")
str2= input("str2")
# i = 0
# output = ""
# while(len(str1)>i and len(str2)>i and (str1[i] == str2[i])):
#     if(((len(str1)-len(str2))/2)>i-1):
#         output+= str1[i]
#         i+=1
#     else:
#         break
# print(output)


#     # len(str1)>i and len(str2)>i and (str1[i] == str2[i])

# class Solution(object):
#     def gcdOfStrings(str1, str2):

#         i = 0
#         output = ""
#         while(len(str1)>i and len(str2)>i and (str1[i] == str2[i]) and str1 + str2 ==str2 + str1):
#             if(((len(str1)-len(str2))/2)>i-1):
#                 output+= str1[i]
#                 i+=1
#             else:
#                 break
#         return output
    
# print(Solution.gcdOfStrings("TAUXXTAUXX","TAUXX"))


if(str1+str2 != str2+str1):
    print("")

#Euklidov algoritam
def gcd(len1,len2):
    while len2:
        len1,len2 = len2,len1%len2
    return len1
    


print(str1[:gcd(len(str1),len(str2))])