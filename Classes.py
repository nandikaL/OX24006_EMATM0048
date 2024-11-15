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

Fish_Dict={}

# for Fishes in dict:
#     pass
    

print(Fin.__dict__)
print(Snapper.__dict__)
print(Brim.__dict__)
print(Cod.__dict__)
print(Flounder.__dict__)
print(Bass.__dict__)

#Warehouse and its costs 
# Supply Main Capacity Aux Capacity Depreciation Warehouse Costs
# Fertiliser 20 litres 10 litres 0.4/quarter £0.10 / litre
# Feed 400 kg 200 kg 0.1/quarter £0.001 / g
# Salt 200 kg 100 kg 0.0/quarter £0.001 / g
#if salt doesnt depreciate is there a need to add this
class Warehouse:
    def __init__(self, warehouse, fertilizer_capacity,feed_capacity,salt_capacity):
        self.warehouse = warehouse
        self.fertilizer_capacity = fertilizer_capacity
        self.feed_capacity = feed_capacity
        self.salt_capacity = salt_capacity
        self.fertilizer_depreciation = 0.4
        self.feed_depreciation = 0.1
        self.salt_depreciation = 0.0
        self.fertilizer_warehouse = 0.1
        self.feed_warehouse = 0.001
        self.salt_warehouse = 0.001

Main_Warehouse = Warehouse('Main',20,400,200)
Aux_Warehouse = Warehouse('Aux',10,200,100)
print(Main_Warehouse.__dict__)
print(Aux_Warehouse.__dict__)

#depreciation = cost x remainder

#fill in later 
class Techician:
    def __init__(self,name):
        self.name = name

class Vendor:
    def __init__(self,name,fertilizer_cost,feed_cost,salt_cost):
        self.name = name
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost
    
    def display(self):
        print(f"{name}: Fertilizer Cost:£{fertilizer_cost}/litre \nFeed Cost:£{feed_cost}/g \nSalt Cost{salt_cost}/g")

# Slippery Lakes £0.30/litre £0.10/g £0.05/g
# Scaly Wholesaler £0.20/litre £0.40/g £0.25/g

Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

print(Slippery.__dict__)
print(Scaly.__dict__)

#This class will be a summary of whats happening in the hatcher
class Hatchery:
    def __init__(self,fish_quantity,supplies,cash,techs):
        self.fish_quantity = fish_quantity
        self.supplies = supplies
        self.cash = cash
        self.techs = techs



#Warehouse and its costs 
# Supply Main Capacity Aux Capacity Depreciation Warehouse Costs
# Fertiliser 20 litres 10 litres 0.4/quarter £0.10 / litre
# Feed 400 kg 200 kg 0.1/quarter £0.001 / g
# Salt 200 kg 100 kg 0.0/quarter £0.001 / g
#if salt doesnt depreciate is there a need to add this