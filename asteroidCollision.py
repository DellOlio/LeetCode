'''
1. dan nam je int array asteroids koji prikazuju
2. za svaki asteroid njegova apsolutna vrijednost oznacuje njegovu velicinu a znak (+/-) pokazuje njegov smijer
3.svi se micu istom brzinom
4. 2 asteroida koji se micu u istu stranu se nikad nece susrest, ako idu jedan prema drugom, veliki preživljava, a ako su iste velicine oba eksplodiraju
'''
asteroids = [1,-1,-2,-2]

def asteroidCollision(asteroids):
    answer = []
    k=0
    while (k<len(asteroids) and asteroids[k]<0):
        answer.append(asteroids[k])
        k+=1
    i = 0
    for i in range(k,len(asteroids)):
        if(asteroids[i]>0 or len(answer)==0):
            answer.append(asteroids[i])
        else:
            if(asteroids[i]<0 and answer[len(answer)-1]<0):
                answer.append(asteroids[i])
            elif(abs(asteroids[i])>abs(answer[len(answer)-1])):
                
                while(len(answer)>0 and abs(asteroids[i])>answer[len(answer)-1] and answer[len(answer)-1]>0):
                    answer.pop()
                
                    
                if(len(answer)==0 or answer[len(answer)-1]<0):
                    answer.append(asteroids[i])
                elif(abs(asteroids[i])==answer[len(answer)-1]):
                    answer.pop()
            elif(abs(asteroids[i])==answer[len(answer)-1]):
                answer.pop()
    return answer
            





print(asteroidCollision(asteroids))