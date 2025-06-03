'''1. Ulaze 2 stringa
2.treba ih spojit tako da ide jedno po jedno slovo ali počinjemo sa word1
3.ako je string duži stavljamo slova na kraj
'''


word1 = input("upisi prvi string")
word2 = input("upisi drugi string")
stringHolder = ""

counter1 = 0
counter2 = 0
while True:
    if(counter1 != len(word1)):
        stringHolder+=word1[counter1]
        counter1+=1
    if(counter2 != len(word2)):
        stringHolder+=word2[counter2]
        counter2+=1    

    if(counter1 == len(word1) and counter2 == len(word2)):
        break

print(stringHolder)