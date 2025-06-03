'''
1.imamo bikera koji ide na put.
2.put se sastoji od n+1 razlicitih visina.
3.biker krece sa tocke 0 sa visinom 0
4.dobivamo int array gain velicine n gdje je gain[n] dobitak visine izmedu tocaka i i i+1(0<=i<n)
5.vracamo najveci položaj


'''



gain = [-4,-3,-2,-1,4,3,2]


def largestAltitude(gain):
    lenght = len(gain)

    for i in range(lenght):
        if i!=0:
            gain[i]=gain[i]+gain[i-1]
        else:
            gain[i]=gain[i]
    if(max(gain))>0:
        return max(gain)
    else:
        return 0



print(largestAltitude(gain))