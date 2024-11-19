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

Fishies = [fin,snapper,brim,cod,flounder,bass]
print(Fishies)

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
    current_stock_dict['fert'] = main_warehouse.fertilizer_capacity + aux_warehouse.fertilizer_capacity #placeholder, find way to add main + aux, is done this way incase we dont max stock
    current_stock_dict['feed'] = main_warehouse.feed_capacity + aux_warehouse.feed_capacity
    current_stock_dict['salt'] = main_warehouse.feed_capacity + aux_warehouse.feed_capacity
    
 #Function to deplete stocks as fishes get sold   
def Deplete_stocks():
    #for loop to loop through each item
    for species in Fishies: 
        #determine value of each fish being bought each cycle   
        demand = species['demand']

        #determine how much of each is needed 
        #demand * fertilizer amount needed per fish    
        fert_need = species['fertilizer'] * demand
        feed_need = species['feed'] * demand
        salt_need = species['salt'] * demand
        maint_need = species['maint_time'] * demand

        if current_stock_dict['fert'] >= fert_need:
                print(f"{species['species']}: {fert_need}ml fertilizer used.")
        else:
            print(f"Not enough fertilizer for {species['species']}. {fert_need}ml needed, only {current_stock_dict['fert']}ml available.")
            continue

        if current_stock_dict['feed'] >= feed_need:
            print(f"{species['species']}: {feed_need}kg feed used.")
        else:
            print(f"Not enough feed for {species['species']}. {feed_need}kg needed, only {current_stock_dict['feed']}kg available.")
            continue

        if current_stock_dict['salt'] >= salt_need:
            print(f"{species['species']}: {salt_need}kg salt used.")
        else:
            print(f"Not enough salt for {species['species']}. {salt_need}kg needed, only {current_stock_dict['salt']}kg available.")
            continue
        #####Maintenence 
        if current_stock_dict['maint_time']>=maint_need:
            print(f"{maint_need} days of work taken")
        else:
            print(f"Not enough labour for {species['species']}. {maint_need} required, only {current_stock_dict['maint_time']} available")
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
        fish_rev = species['price'] * demand 
        add_rev = current_stock_dict['cash']+fish_rev
        current_stock_dict['cash']+add_rev

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


def Payments():
    standard = 1500 #put this into a class somewhere?
    tech_payments = len(Hatchery.current_techs)*4500 #500 mulitpled by 9 weeks
    #can i loop this through the classes?? 
    warehouse_fert = current_stock_dict['fert']*main_warehouse.costs.fertilizer_warehouse 
    warehouse_feed = current_stock_dict['feed']*main_warehouse.costs.feed_warehouse
    warehouse_salt = current_stock_dict['salt']*main_warehouse.costs.salt_warehouse 
    #can be looped?? 
    total_warehouse = warehouse_fert + warehouse_feed + warehouse_salt
    total_payments = standard + tech_payments + total_warehouse
    print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Depreciation: £{total_depreciation}\nTotal Warehouse Costs: £{total_warehouse}")
    
    new_cash_value = current_stock_dict['cash'] - total_payments
    current_stock_dict['cash'] = new_cash_value
    print(f"Current Balance: {current_stock_dict['cash']}")
    

Current_stocks()
Deplete_stocks()
Payments() #put in a if/else checkpoint, if currently in the negatives, bankrupt! bad ending

#Now restock your supples : 
#Display inventory in the two warehouses 
#function to see how much is left 
#if amount less > than aux capacity (meaning aux warehouse still has things inside)
    #diff function
#if amount less < aux capacity (meaning aux warehouse is empty )

#depreciation happenings: 
def Depreciate ():
    depreciation_fert = current_stock_dict['fert']-(current_stock_dict['fert']*main_warehouse.costs.fertilizer_depreciation) #using main warehouse since does not matter where from
    depreciation_feed = current_stock_dict['feed']-(current_stock_dict['feed']*main_warehouse.costs.feed_depreciation)
    depreciation_salt = current_stock_dict['salt']-(current_stock_dict['salt']*main_warehouse.costs.salt_depreciation)

def Warehouse_left():
    if current_stock_dict['fert'] >= aux_warehouse.fertilizer_capacity:
        aux_warehouse.fertilizer_capacity -= current_stock_dict['fert']
        if aux_warehouse.fertilizer_capacity <= 0:
            aux_warehouse.fertilizer_capacity = 0
    else:
        main_warehouse.fertilizer_capacity -= current_stock_dict['fert']
        if main_warehouse.fertilizer_capacity <= 0:
            main_warehouse.fertilizer_capacity = 0 
   
    if current_stock_dict['feed'] >= aux_warehouse.feed_capacity:
        aux_warehouse.feed_capacity -= current_stock_dict['feed']
        if aux_warehouse.feed_capacity <= 0:
            aux_warehouse.feed_capacity = 0

    else:
        main_warehouse.feed_capacity -= current_stock_dict['feed']
        if main_warehouse.feed_capacity <= 0:
            main_warehouse.feed_capacity = 0
    
    if current_stock_dict['salt'] >= aux_warehouse.salt_capacity:
        aux_warehouse.salt_capacity -= current_stock_dict['salt']
        if aux_warehouse.salt_capacity <= 0:
            aux_warehouse.salt_capacity = 0
    else:
        main_warehouse.salt_capacity -= current_stock_dict['salt']
        if main_warehouse.salt_capacity <= 0:
            aux_warehouse.salt_capacity = 0
    
    print(f"Fertilizer left in Main Warehouse: {main_warehouse.fertilizer_capacity}")
    print(f"Fertilizer left in Auxillary Warehouse: {aux_warehouse.fertilizer_capacity}")
    print(f"Feed left in Main Warehouse: {main_warehouse.feed_capacity}")
    print(f"Feed left in Auxillary Warehouse: {aux_warehouse.feed_capacity}")
    print(f"Salt left in Main Warehouse: {main_warehouse.salt_capacity}")
    print(f"Salt left in Auxillary Warehouse: {aux_warehouse.salt_capacity}")

Warehouse_left()

#Choose which vendor to buy from
#Print Prices
restock_Fertilizer = input('Where would you like to purchase your Fertilizer from?')
print(Slippery.display())
print(Scaly.display())

restock_Feed = input('Where would you like to purchase your Feed from?')
restock_Salt = input('Where would you like to purchase your Salt from?')
#Display vendors (select 1 or 2) 