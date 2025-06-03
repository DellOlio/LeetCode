'''
1.dan je string s(samo mala slova) i int k
2.treba vratit najveci skup samoglasniga u substringu od s velicine k 


'''

s = "leetcode"
k = 3
vowles = list("aeiou")



def maxVowels(s,k):
    
    s = list(s)
    cur_substring = s[:k]
    
    maximum_vowels=len([j for j in cur_substring if j in vowles])
    cur_vowels = maximum_vowels
    for i in range(k,len(s)):
        if(s[i] in vowles):
            cur_vowels+=1
        if(s[i-k] in vowles):
            cur_vowels-=1
        maximum_vowels = max(maximum_vowels,cur_vowels)
    return(maximum_vowels)
        



print(maxVowels(s,k))