'''
imamo klasu RecentCounter koja broji broj nedavnih zahtjeva u određenom vremenu

implementiramo RecentCounter() koji inicijalizira counter sa 0 zahtjeva
def ping(int t)->int: dodaje zahtjev na vrijeme t gdje t predstavlja neko vrijeme u milisekundama i vraca broj zahtjeva koji su se desili u zadnjih 3000ms(i ovaj trenutni)
treba vratit broj zahtjeva koji su se desili u [t-3000,t]
garantirano je da ce svaki sljedeci t bit veci
'''

t = 0
class RecentCounter:

    def __init__(self):
        self.recentRequests = []
        return None
        
        
        

    def ping(self, t: int) -> int:
        #dosta sporo
        # counter = 0
        # for i in self.recentRequests:
        #     if i + 3000>= t:
        #         counter+=1
        # self.recentRequests.append(t)
        
        
        while len(self.recentRequests)!=0 and self.recentRequests[0] + 3000 < t:
            self.recentRequests.pop(0)
            
        self.recentRequests.append(t)
        return len(self.recentRequests)
        






# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()

param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3001)
param_1 = obj.ping(3002)

print(param_1)