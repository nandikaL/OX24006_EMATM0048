#Import
from FishClass import Fish
from WarehouseClass import Warehouse
from TechicianClass import Technician
from VendorClass import Vendor
from HatcheryClass import Hatchery
#from QuarterClass import Quarter

#Instances 

fin_i = Fish('Clef Fins',100.0,12,2,2.0,25,250)
snapper_i = Fish('Timpani Snapper', 50.0, 9, 2, 1.0, 10, 350)
brim_i = Fish('Andalusian Brim', 90.0, 6, 2, 0.5, 15, 250)
cod_i = Fish('Plagal Cod', 100.0, 10, 2, 2.0, 20, 400)
flounder_i = Fish('Fugue Flounder', 200.0, 12, 2, 2.5, 30, 550)
bass_i = Fish('Modal Bass', 300.0, 12, 6, 3.0, 50, 500) 

fin = fin_i.__dict__
snapper = snapper_i.__dict__
brim = brim_i.__dict__
cod = cod_i.__dict__
flounder = flounder_i.__dict__
bass = bass_i.__dict__

fishies = [fin,snapper,brim,cod,flounder,bass]
print(fishies)

main_warehouse = Warehouse('Main',20,400,200)
aux_warehouse = Warehouse('Aux',10,200,100)

# print(Main_Warehouse.__dict__)
# print(Aux_Warehouse.__dict__)

Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

# print(Slippery.__dict__)
# print(Scaly.__dict__)

Hatchery = Hatchery('supplies', 'cash', 'techs')

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
Hatchery.Tech_Again()

#How many fish sold # make function for changing demand??? 
#standardized amount 
#deplete_stocks(fishy=Fish.self) #how do i do this???

#Creating a dictonary of the things that flow in the hatchery
current_stock_dict = {'maint_time':0, 'fert':0, 'feed':0, 'salt':0, 'cash':10000}

#Function to update stocks in warehouse ? 
def Current_stocks():
    #Append to dictionary number of labour days available
    current_stock_dict['maint_time']=len(Hatchery.current_techs)*45 #45 days of work per person

    #Adding sum of items in the warehouse 
    current_stock_dict['fert'] = 30 #placeholder, find way to add main + aux, is done this way incase we dont max stock
    current_stock_dict['feed'] = 600
    current_stock_dict['salt'] = 300
    
 #Function to deplete stocks as fishes get sold   
def deplete_stocks():
    #for loop to loop through each item
    for species in fishies: 
        #determine value of each fish being bought each cycle   
        demand = fishies['demand']

        #determine how much of each is needed 
        #demand * fertilizer amount needed per fish    
        fert_need = fishies['fertilizer'] * demand
        feed_need = fishies['feed'] * demand
        salt_need = fishies['salt'] * demand
        maint_need = fishies['maint_time'] * demand

        if current_stock_dict['fert'] >= fert_need:
                print(f"{fishies['species']}: {fert_need}ml fertilizer used.")
        else:
            print(f"Not enough fertilizer for {fishies['species']}. {fert_need}ml needed, only {current_stock_dict['fert']}ml available.")
            continue

        if current_stock_dict['feed'] >= feed_need:
            print(f"{fishies['species']}: {feed_need}kg feed used.")
        else:
            print(f"Not enough feed for {fishies['species']}. {feed_need}kg needed, only {current_stock_dict['feed']}kg available.")
            continue

        if current_stock_dict['salt'] >= salt_need:
            print(f"{fishies['species']}: {salt_need}kg salt used.")
        else:
            print(f"Not enough salt for {fishies['species']}. {salt_need}kg needed, only {current_stock_dict['salt']}kg available.")
            continue
        #####Maintenence 
        if current_stock_dict['maint_time']>=maint_need:
            print(f"{maint_need} days of work taken")
        else:
            print(f"Not enough labour for {fishies['species']}. {maint_need} required, only {current_stock_dict['maint_time']} available")
            continue

        new_fert_value = current_stock_dict['fert'] - fert_need
        current_stock_dict['fert'] = (new_fert_value)
        new_feed_value = current_stock_dict['feed'] - feed_need
        current_stock_dict['feed'] = (new_feed_value)
        new_salt_value = current_stock_dict['salt'] - salt_need
        current_stock_dict['salt'] = (new_salt_value)
        new_maint_value = current_stock_dict['maint_time']-maint_need
        current_stock_dict['maint_time'] = (new_maint_value)

        ##add money
        fish_rev = fishies['price'] * demand 
        add_rev = current_stock_dict['cash']+fish_rev
        current_stock_dict['cash']+fish_rev

    #ok so: fish have fert, feed, salt
    #1st type of fish: input number being sold:
    #function loop starts: number of fish * fert 
    #if enough fert in warehouses, move to next item, feed. 
    #if enough feed in warehouses, move to next item 
    #if enough salt in warehouses, move to next item
    #must meet all variables before continue
    #then  do labour
    #the append everything
    #loopy loop


    def payments():
        standard = 1500 #put this into a class somewhere?
        tech_payments = len(Hatchery.current_techs)*4500 #500 mulitpled by 9 weeks
        depreciation_fert = current_stock_dict['fert']-(current_stock_dict['fert']*Warehouse.fertilizer_depreciation) #leftover-(leftover{fishies['species'].depreciation)
        depreciation_feed = current_stock_dict['feed']-(current_stock_dict['feed']*Warehouse.fertilizer_depreciation)
        depreciation_salt = current_stock_dict['salt']-(current_stock_dict['salt']*Warehouse.fertilizer_depreciation)
        total_depreciation = depreciation_fert + depreciation_feed + depreciation_salt
        #can i loop this through the classes?? 
        warehouse_fert = current_stock_dict['fert']*Warehouse.fertilizer_warehouse 
        warehouse_feed = current_stock_dict['fed']*Warehouse.feed_warehouse
        warehouse_salt = current_stock_dict['salt']*Warehouse.salt_warehouse #leftover x{fishies['species'].warehousecost
        #can be looped?? 
        total_warehouse = warehouse_fert + warehouse_feed + warehouse_salt
        total_payments = standard + tech_payments + total_depreciation + total_warehouse
        print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Depreciation: £{total_depreciation}\nTotal Warehouse Costs: £{total_warehouse}")
        
        new_cash_value = current_stock_dict['cash'] - total_payments
        current_stock_dict['cash'] = new_cash_value
        #loop through the current stocks dictionary to find the remaining supplies 

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