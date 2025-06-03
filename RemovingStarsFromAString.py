'''
1. dan nam string s koji ima u sebi *
2. u jednoj operaciji možemo izabrati * u s i maknuti najbliži lijevi karakter i zvjezdicu
3.vracamo string nakon sto su sve zvjezdice maknute
4.ulaz ce biti takav da je takva operacija uvijek moguća

'''

s = "leet**cod*e"


#pre sporo
# def removeStars(s):
#     s = list(s)
#     i = 1
#     while "*" in s:
#         if(s[i]== "*"):
#             s.pop(i-1)
#             s.pop(i-1)
#             i-=1
#         else:
#             i+=1
#     s = "".join(s)
#     return(s)


def removeStars(s):
    answer = []

    for i in s:
        if i != "*":
            answer.append(i)
        else:
            answer.pop()
    return "".join(answer)
            



print(removeStars(s))