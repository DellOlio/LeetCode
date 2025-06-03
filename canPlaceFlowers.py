'''
1.imamo int array 0 i 1 gdje 0 znaci prazno a jedan znaci popunjeno
2.imamo int n koji nas pita dali mozemo toliko cvijetova zasadit bez da prekrsimo pravilo koje je da nesmije bit cvijet kraj cvijeta
3.vracamo true ili false po dobivenom n-u i arrayu


'''


flowerbed = [0,1,1,1]
#len je 7
n= 1
counter = 0

for i in range(len(flowerbed)):
    if(len(flowerbed)==1):
        counter += abs(flowerbed[i]-1)
    elif(i == 0):
        if(flowerbed[i+1]==0 and flowerbed[i]!=1):
            counter+=1
            flowerbed[i] = 1
    elif(i == len(flowerbed)-1):
        if(flowerbed[i-1]==0 and flowerbed[i]!=1):
            counter+=1
            flowerbed[i] = 1    
    elif (flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1):
        counter+=1
        flowerbed[i] = 1 
print(counter)



