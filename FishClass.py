class Fish: 
    
    def __init__(self,species,fertilizer,feed,salt,maintaince_time,demand,price):
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintaince_time = maintaince_time
        self.demand = demand
        self.price = price

    def description(self):
        print(f"{self.species}: Fertilizer Use:{self.fertilizer}ml \nFeed use: {self.feed}kg \nSalt Use:{self.salt}kg \nMaintainence Time: {self.maintaince_time}")

    def Price(self):
        print(f"{self.species}: Price:${self.price}")

Fin = Fish('Clef Fins',100.0,12,2,2.0,25,250)
Snapper = Fish('Timpani Snapper', 50.0, 9, 2, 1.0, 10, 350)
Brim = Fish('Andalusian Brim', 90.0, 6, 2, 0.5, 15, 250)
Cod = Fish('Plagal Cod', 100.0, 10, 2, 2.0, 20, 400)
Flounder = Fish('Fugue Flounder', 200.0, 12, 2, 2.5, 30, 550)
Bass = Fish('Modal Bass', 300.0, 12, 6, 3.0, 50, 500)   

print(Fin.__dict__)
print(Snapper.__dict__)
print(Brim.__dict__)
print(Cod.__dict__)
print(Flounder.__dict__)
print(Bass.__dict__)