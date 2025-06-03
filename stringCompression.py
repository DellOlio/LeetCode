'''
1.array chars treba compressat(ako imamo aaaa to treba vratit kao a4), ako je kolicina veca od 10 treba razdvojit na 2 karaktera recimo 12 je 1,2
2.pocinjemo sa praznim stringom s
3.treba vratit duzinu novog arraya
'''

         

# def SC(chars: list[str])->int:
#     s = ""
#     counter = 0
    
#     while chars:
#         temp = chars[0]
#         s = s+chars[0]
#         while(chars and chars[0] == temp):
#             counter+=1
#             chars.pop(0)
#         if counter>1:
#             s = s+str(counter)
#         counter = 0
        
#     chars.clear()
#     for letter in s:
#         chars.append(letter)
#     return len(s)

# print(SC(chars))
            
# print(chars)
#treba raditi u danoj listi


# chars = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]


# def SC(chars):
#     step_counter=0
#     position=0
#     lenght = len(chars)
#     while(step_counter<lenght):
#         counter=0
#         temp = chars[position]
#         while len(chars)>position and temp==chars[position]:
#             chars.pop(position)
#             step_counter+=1
#             counter+=1
#         chars.insert(position,temp)
#         position+=1
#         if(counter>1 and counter<10):
#             chars.insert(position,str(counter))
#             position+=1
#         elif(counter>1):
#             for character in str(counter):
#                 chars.insert(position,character)
#                 position+=1
            
#     return len(chars)

            
# print (SC(chars))
# print(chars)     



#ne smije se brisati nista iz liste ni ubacivat


chars = ["a","a","b","b","c","c","c"]


def SC(chars):
    step_counter=0
    position=0
    lenght = len(chars)
    while(step_counter<lenght):
        counter=0
        temp = chars[step_counter]
        while len(chars)>step_counter and temp==chars[step_counter]:
            step_counter+=1
            counter+=1
        chars[position] = temp
        position+=1
        if(counter>1):
            for character in str(counter):
                chars[position]= character
                position+=1
            
    return position

            
print (SC(chars))
print(chars)     


