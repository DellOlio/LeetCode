'''
1. dan nam je kodirani string i trebamo ga dekodirati
2. pravilo je: k[encoded_string] gdje encoded_string u [] je ponovljena k puta.(k>0)
3. možemo predpostaviti da je ninput string uvijek validan i da podatci ne sadrže brojke jer su one samo za količinu


'''


#imamo curString = ""
#imamo curNum = 0
#i imamo stack = []
#idemo kroz string i ako je slovo upisujemo u curStiring
#ako je broj u cur number
#kad dodemo do [ onda upisujemo prvo string u stack i onda broj u stack
#i praznimo curstring i cur num
# i kad naletimo na ] onda iz stacka vadimo curnum i cur string
# i onda nam je curstring = slovu iz stacka + num * curstring
s = "100[leetcode]"
def decodeString(s):
    curString= ""
    curNum = 0
    stack = []
    for i in s:
        if(i.isalpha()):
            curString+=i
        elif(i.isdigit()):
            curNum=curNum*10+int(i)
        elif(i=="["):
            stack.append(curString)
            stack.append(curNum)
            curString = ""
            curNum = 0
        elif (i=="]"):
            numHolder = stack.pop()
            stringHolder = stack.pop()
            curString = stringHolder + numHolder*curString
    return curString





print(decodeString(s))