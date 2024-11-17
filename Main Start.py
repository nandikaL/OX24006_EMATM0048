#All classes placed here as importing is not working

######Fish Class

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

###### Warehouse Class

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

##### Technician Class
class Technician:
    def __init__(self,name):
        self.name = name
        self.work_days = 45 #9weeks x 5day/week
        self.pay = 500

###### Vendor Class

class Vendor:
    def __init__(self,name,fertilizer_cost,feed_cost,salt_cost):
        self.name = name
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost
    
    def display(self):
        print(f"{self.name}: Fertilizer Cost:£{self.fertilizer_cost}/litre \nFeed Cost:£{self.feed_cost}/g \nSalt Cost{self.salt_cost}/g")

Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

##### Hatchery Class

class Hatchery:
    def __init__(self,supplies,cash,techs):
        self.supplies = supplies
        self.cash = cash
        self.techs = techs
    
    current_techs = []
    current_techs_len = len(current_techs)

    def tech_display():
        for item in Hatchery.current_techs:
            print(f'Hired:{item},Pay:£{Hatchery.self.pay}')
    
    def Tech_Roster():
        print('Please choose how many technicians you would like to add or remove')
        print('To add, please type a positive number. Example: To add 2, type 2')
        print('To remove, please type a negative number. Example: To remove 2, type -2')
        print('Please note, there must be between 1 to 5 technicians')  
        print('Current Technicians:')
        print(Hatchery.current_techs)
        num = int(input().strip())
        total = (num+Hatchery.current_techs_len)
        if total < 1:
            print(f'There must be at least one technician')
            return Hatchery.Tech_Roster()
        elif total > 5:
            print(f'There cannot be more than 5 technicians. If you add {num} technicians, there will be {total}')
            return Hatchery.Tech_Roster()
        else:
            if num == 0:
                print("No changes made")
                print(Hatchery.current_techs)
            elif num > 0:
                while num > 0:
                    print('Please enter the name of the tech you want to hire:')
                    print('If more than one please enter one name at a time.')
                    new_tech = input().strip().lower()
                    if new_tech in Hatchery.current_techs:
                        print('We already hired them')
                    else:
                        num -= 1
                        Hatchery.current_techs.append(new_tech)
                        new_tech = Technician(new_tech)
                        print(Hatchery.current_techs)
            elif num < 0:
                while num < 0:
                    fire_tech = input().strip().lower()
                    if fire_tech in Hatchery.current_techs:
                        Hatchery.current_techs.remove(fire_tech)
                        num += 1
                    else:
                        print('We never hired this stranger')
            else:
                print('Invalid response')

####
# Very rough plan. 
#Inputs
print("Welcome to Fish Tycoon, Please Try Not to Go Bankrupt.")
print("Have fun!")
#Import in Hatchery (hatchery class has everything) 

#Asks for number of quaters to run the cycle
quaters = input('Please type in the number of quaters to run this simulation for')

#How many technicians would you like to add or remove?
Hatchery.Tech_Roster()
# while True:
#     technician_number=int(input('Please write the NUMBER of technicians you would like to hire'))
#     for x in range (technician_number):
#         #Technician names 
#         tech_name = input('Please type the name of the technician you would like to hire')
#         #if in dict or class of tech names, do nothing
#         #else, all into dict or class 
#         print(f"Hired {tech_name.title()}, Days of Work = 45, Total Payment = 500")
#     break
#"Hired ___, Total Payment: 500x9, total days of working 5x9=45

#How many fish sold
#standardized amount 

#some function to calculate the costs per fish sold, loop until run out of any item then say insufficient 

#say say what was unsold 

#current supplies in warehouses

#current hatchery cash 1

#Amount to pay for technicians: 4500 x number of technicians))
#Amount for utilities: 1500 
#Amount to pay for depreciation: ?? 
#Hashery cash - all these above = updated hashery amount 

#Choose which vendor to buy from
#Print Prices
restock_Fertilizer = input('Where would you like to purchase your Fertilizer from?')

print(Slippery.display())
print(Scaly.display())

restock_Feed = input('Where would you like to purchase your Feed from?')
restock_Salt = input('Where would you like to purchase your Salt from?')
#Display vendors (select 1 or 2) 