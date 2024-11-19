class Fish: 
    
    def __init__(self,species,fertilizer,feed,salt,maint_time,demand,price):
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maint_time = maint_time
        self.demand = demand
        self.price = price

    def description(self):
        print(f"{self.species}: Fertilizer Use:{self.fertilizer}ml \nFeed use: {self.feed}kg \nSalt Use:{self.salt}kg \nMaintainence Time: {self.maint_time}")

    def Price(self):
        print(f"{self.species}: Price:${self.price}")