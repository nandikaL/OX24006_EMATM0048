"""OX24006, Nandika, This file contains the Fish class"""

#Define Fish
class Fish: 
    #Define the items inside each fish class
    def __init__(self,species,fertilizer,feed,salt,maint_time,demand,price):
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maint_time = maint_time
        self.demand = demand
        self.price = price

    #Defined a function here to displau what each fish needs to be raised, and price #Consider adding into main to display before selling
    def description(self):
        print(f"{self.species}: Fertilizer Use:{self.fertilizer}ml \nFeed use: {self.feed}kg \nSalt Use:{self.salt}kg \nMaintainence Time: {self.maint_time} \nSelling Price{self.price}")