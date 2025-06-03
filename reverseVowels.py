'''
1. dobivamo string s i trebamo zamjenit mjesta svih samo glasnika - ako imamo asijofe trebamo dobit esojifa
2. mogu bit upper ili lower i moze ih bit vise puta
'''
s = "IceCreAm"
s = list(s)
vowels = ["a","e","i","o","u","A","E","I","O","U"]

start = 0
end = len(s)-1

while start<end:
    if(s[start]) in vowels:
        if(s[end]) in vowels:
            temp = s[start]
            s[start] = s[end]
            s[end]=temp
            end-=1
            start+=1


        else:
            end-=1
    else:
        
        start+=1
result = "".join(s)          
print(result)




