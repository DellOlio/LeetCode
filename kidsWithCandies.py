'''
1.imamo n dijece
2. imamo array candies gdje je svaki candies[i] pokazuje 
kolko i-to dijete ima candia
3.imamo integer extraCandies koji nam govori kolko imamo viska
4.vracamo boolean array velicine n gdje vracamo true ako i-to dijete ima 
najvise candia nakon sto mu damo sve ekstra candye

'''

candies = [3,2,4,6,1]
extraCandies = 3

result = [(i+extraCandies)>=max(candies) for i in candies ]
print(result)