'''
1. dobivamo string s i string t
2. trebamo vratit true ako je s subsequence t (ace je subsequence od abcue)




'''


s = "axc"
t = "ahbgdc"


def isSubsequence(s,t):
    lentgtOfS = len(s)
    j = 0
    if(s == ""):
        return True
    for i in range(len(t)):
        if(t[i]==s[j]):
            j+=1
        if(j==lentgtOfS):
            return True
    return False


print(isSubsequence(s,t))