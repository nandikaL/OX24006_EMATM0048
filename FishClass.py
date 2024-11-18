class Fish: 
    
    def __init__(self,species,fertilizer,feed,salt,maintenance_time,demand,price):
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintenance_time = maintenance_time
        self.demand = demand
        self.price = price

    def description(self):
        print(f"{self.species}: Fertilizer Use:{self.fertilizer}ml \nFeed use: {self.feed}kg \nSalt Use:{self.salt}kg \nMaintainence Time: {self.maintenance_time}")

    def Price(self):
        print(f"{self.species}: Price:${self.price}")