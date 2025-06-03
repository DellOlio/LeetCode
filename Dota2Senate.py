'''
u doti2 su 2 strane : radiant i dire
senat se sastoji od senatora iz obje strane i želi odlucit za neku promjenu
glasanje se radi tako da u svakoj rundi jedan senator može :banat jednog senatora za cijelo glasanje
                                                           :proglasit pobjedu: ako je protumacio da svi senatori koji jos uvijek imaju pravo glasa su iz iste strane
dan nam je string senate koja predstavlja kojoj strani koji senator pripada(R/D), veličina stringa je broj senatora
Procedura pocinje od prvog do zadnjeg senatora redoljedom stringa. svi senatori koji su izgubili prava ce bit preskoceni
Predpostavljamo da je svaki senator dovoljno pametan i da če koristit najbolju strategiju za njegovu stranu.
Vracamo Radiant ili Dire po tome ko je pobjedio

'''
senate = "RDD"
def predictPartyVictory(senate):
    r_positions = []
    d_positions=[]
    for i in range(len(senate)):
        if senate[i]=="R":
            r_positions.append(i)
        else:
            d_positions.append(i)
    cur_position = len(senate)
    print(r_positions,d_positions)
    while len(r_positions)!=0 and len(d_positions)!=0:
        if r_positions[0]<d_positions[0]:
            d_positions.pop(0)
            r_positions.pop(0)
            r_positions.append(cur_position)
            cur_position+=1
        else:
            r_positions.pop(0)
            d_positions.pop(0)
            d_positions.append(cur_position)
            cur_position+=1
    if(len(r_positions)>0):
        return "Radiant"
    else:
        return "Dire"
    


print(predictPartyVictory(senate))






