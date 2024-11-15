#Planning the classes, to be be seperated

#Start with classes, seperate later 

#Fish Types and its maintainence: 
    #Clef Fins 100.0 12 2 2.0
    # Timpani Snapper 50.0 9 2 1.0
    # Andalusian Brim 90.0 6 2 0.5
    # Plagal Cod 100.0 10 2 2.0
    # Fugue Flounder 200.0 12 2 2.5
    # Modal Bass 300.0 12 6 3.0
class Fish: 
    
    def __init__(self,species,fertilizer,feed,salt,maintaince_time,demand,price):
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintaince_time = maintaince_time

    def description(self):
        print(f"{self.species}: Fertilizer Use:{self.fertilizer}ml \nFeed use: {self.feed}kg \nSalt Use:{self.salt}kg \nMaintainence Time: {self.maintaince_time}")

        

#Warehouse and its costs 
# Supply Main Capacity Aux Capacity Depreciation Warehouse Costs
# Fertiliser 20 litres 10 litres 0.4/quarter £0.10 / litre
# Feed 400 kg 200 kg 0.1/quarter £0.001 / g
# Salt 200 kg 100 kg 0.0/quarter £0.001 / g
#if salt doesnt depreciate is there a need to add this
class Warehouse:
    def __init__(self,fertilizer_capacity,feed_capacity,salt_capacity,fertilizer_depreciation,feed_depreciation,salt_depreciation,fertilizer_depreciation_cost,feed_depreciation_cost,salt_depreciation_cost):
        self.fertilizer_capacity = fertilizer_capacity
        self.feed_capacity = feed_capacity
        self.salt_capacity = salt_capacity
        self.fertilizer_depreciation = fertilizer_depreciation
        self.feed_depreciation = feed_depreciation
        self.salt_depreciation = salt_depreciation
        self.fertilizer_depreciation_cost = fertilizer_depreciation_cost
        self.feed_depreciation_cost = feed_depreciation_cost
        self.salt_depreciation_cost = salt_depreciation_cost

#fill in later 
class Techician:
    def __init__(self,name):
        self.name = name

class Vendor:
    def __init__(self,fertilizer_cost,feed_cost,salt_cost):
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost

#This class will be a summary of whats happening in the hatcher
class Hatchery:
    def __init__(self,fish_quantity,supplies,cash,techs):
        self.fish_quantity = fish_quantity
        self.supplies = supplies
        self.cash = cash
        self.techs = techs

FishType = Fish(species='Clef Fins', fertilizer='100.0', feed='12', salt='2', maintaince_time='2.0', demand=25, price=250)
print(FishType.__dict__)
FishType.description()