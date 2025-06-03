'''
1. 2 stringa se gledaju da su blizu ako:
 zamjenimo mjesto bilo koja 2 postoječa karaktera (abcde -> aecdb - mozemo zamjenit b i e)
 pretvorimo svako ponavljanje jednog postojeceg karaktera u drugi postojeci karakter

2.dobivamo 2 stringa word1 i word 2
3. vracamo ako su si blizu a false ako nisu
4. mozemo koristit ponudene operacije bilo koliko puta
'''


word1 ="aaabbbbccddeeeeefffff"
word2 ="aaaaabbcccdddeeeeffff"


def closeStrings(word1,word2):
    #1.ako su sva slova ista ali im je kriva pozicija
    #2.ako ima isti brj ponavljanja 2 razlicita slova
    if len(word1)!=len(word2):
        return False
    word1hash= dict()
    word2hash = dict()
    for i in range(len(word1)):
        if(word1[i] not in word1hash):
            word1hash[word1[i]]=1
        else:
            word1hash[word1[i]]+=1
        if(word2[i] not in word2hash):
            word2hash[word2[i]]=1
        else:
            word2hash[word2[i]]+=1
        
    # print(sorted(word1hash),sorted(word2hash))
    # print(sorted(word1hash.keys()) not in sorted(word2hash.keys()))

    # print(set(sorted(word1hash.values())) - set(sorted(word2hash.values())))
    print(sorted(word1hash.values()),sorted(word2hash.values()))
    word1hashKeys = sorted(word1hash.keys())
    word1hashValues = sorted(word1hash.values())
    word2hashKeys = sorted(word2hash.keys())
    word2hashValues = sorted(word2hash.values())
    for j in range(len(word1hash.values())):
        if(word1hashKeys[j]!=word2hashKeys[j] or word1hashValues[j]!=word2hashValues[j]):
            return False
    
    
    # print(word1hash.keys())
    return True
        
    # for j in range(len(word1hash)):
    #     print(list(word1hash.keys())[j], list(word2hash.keys()))
    #     print(list(word1hash.values())[j], list(word2hash.values()))

    #     print(set(word2hash.values())-set(word1hash.values()))
    #     if(list(word1hash.keys())[j] not in list(word2hash.keys()) or len(set(word1hash.values())-set(word2hash.values())) or len(set(word2hash.values())-set(word1hash.values()))):
            
    #         return False
    # return len(word1hash.keys())==len(word2hash.keys())




print(closeStrings(word1,word2))