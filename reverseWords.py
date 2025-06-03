'''
1.input string
2.rijeci su razdvojeni bar jednim razmakom
3.vratit sa jednim razmakom od kraja(polozaj zamjenit tako da je pocetak kraj)



'''

s = "a good   example"
s = list(s.split())
print(s)
result = ""
for i in range(len(s)-1,0-1,-1):
    result+=s[i]+" "

print(result.rstrip())
