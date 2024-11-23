#Import
from FishClass import Fish
from WarehouseClass import Warehouse
#from TechicianClass import Technician
from VendorClass import Vendor
from HatcheryClass import Hatchery
#from QuarterClass import Quarter

#Instances 

#units are ml,kg,kg,days, not applicable to demand, pounds
fin = Fish('Clef Fins',100.0,12,2,2.0,25,250).__dict__ 
snapper = Fish('Timpani Snapper', 50.0, 9, 2, 1.0, 10, 350).__dict__
brim = Fish('Andalusian Brim', 90.0, 6, 2, 0.5, 15, 250).__dict__
cod = Fish('Plagal Cod', 100.0, 10, 2, 2.0, 20, 400).__dict__
flounder = Fish('Fugue Flounder', 200.0, 12, 2, 2.5, 30, 550).__dict__
bass = Fish('Modal Bass', 300.0, 12, 6, 3.0, 50, 500).__dict__

Fishies = [fin,snapper,brim,cod,flounder,bass]

#loop to convert all the ml to liters, for convience later
for fish in Fishies:
    fish['fertilizer'] = fish['fertilizer']/1000                                                                                            

#units: liters, kg, kg
main_warehouse = Warehouse('Main',20,20,400,400,200,200)
aux_warehouse = Warehouse('Aux',10,10,200,200,100,100)

# print(Main_Warehouse.__dict__)
# print(Aux_Warehouse.__dict__)

#units: pound per liter, pound per kg, pound per kg
Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

# print(Slippery.__dict__)
# print(Scaly.__dict__)

Nans_Hatchy = Hatchery('supplies', 10000)

def make_pretty(title):
    print(f"\n{'=' * 60}")
    print(f"{title.center(60)}")
    print(f"{'=' * 60}")

#Creating a dictonary of the things that flow in the hatchery
current_stock_dict = {'maint_time':0, 'fert':0, 'feed':0, 'salt':0, 'cash':Nans_Hatchy.cash} #inside a class? 
def display_stocks():
    print(f"Maintenance Time Available: {current_stock_dict['maint_time']} days")
    print(f"Fertilizer Available: {current_stock_dict['fert']} liters")
    print(f"Feed Available: {current_stock_dict['feed']} kg")
    print(f"Salt Available: {current_stock_dict['salt']} kg")
    print(f"Cash Balance: £{current_stock_dict['cash']}")            

#Import in Hatchery (hatchery class has everything) 

#How many fish sold # make function for changing demand??? 
#standardized amount 
#deplete_stocks(fishy=Fish.self) #how do i do this???

#Function to update stocks in warehouse ? 
def Current_stocks():
    #Append to dictionary number of labour days available
    current_stock_dict['maint_time']=len(Nans_Hatchy.current_techs)*45 #45 days of work per person

    #Adding sum of items in the warehouse 
    current_stock_dict['fert'] = main_warehouse.fert_amount + aux_warehouse.fert_amount #allows for not full replenishing
    current_stock_dict['feed'] = main_warehouse.feed_amount + aux_warehouse.feed_amount
    current_stock_dict['salt'] = main_warehouse.salt_amount + aux_warehouse.salt_amount

    print()


 #Function to deplete stocks as fishes get sold   
def Deplete_stocks():
    #for loop to loop through each item
    for species in Fishies: 

        #determine value of each fish being bought each cycle   
        #Display fish demands
        print("-" * 60)
        user_demand = input(f"How many {species['species']} are you selling this quarter? \nDon't enter anything for default demand of {species['demand']}").strip()
        if user_demand == '':
            demand = species['demand']
            print('Default selected')
        elif int(user_demand) > species['demand']:
            print('You tried to sell alot of fish! But there were no takers. You sold the default')
            demand = species['demand']
        else: 
            try:
                demand = int(user_demand) 
                if int(demand) < 0:
                    print('It needs to be a positive number. Default demand selected.')
                    demand = species['demand']
            except ValueError:
                print('It needs to be a number. Default demand selected')
                demand = species['demand']
            

        #determine how much of each is needed 
        #demand * fertilizer amount needed per fish    
        fert_need = species['fertilizer'] * demand
        feed_need = species['feed'] * demand
        salt_need = species['salt'] * demand
        maint_need = species['maint_time'] * demand

        if current_stock_dict['fert'] >= fert_need:
            print(f"{species['species']}: {fert_need}l fertilizer used.")
        else:
            print(f"The {species['species']} died from lack of poor air quality! \n{species['species']} need {fert_need}liters of fertilizer, only {current_stock_dict['fert']}l available.")
            continue

        if current_stock_dict['feed'] >= feed_need:
            print(f"{species['species']}: {feed_need}kg feed used.")
        else:
            print(f"The {species['species']} died from malnourishment! \n{species['species']} need {feed_need}kg of feed, only {current_stock_dict['feed']}kg available.")
            continue

        if current_stock_dict['salt'] >= salt_need:
            print(f"{species['species']}: {salt_need}kg salt used.")
        else:
            print(f"The {species['species']} died from reverse osmosis! \n{species['species']} need {salt_need}kg of salt, only {current_stock_dict['salt']}kg available.")
            continue
        #####Maintenence 
        if current_stock_dict['maint_time']>=maint_need:
            print(f"{maint_need} days of work taken")
        else:
            print(f"Your staff are overworked! {species['species']} need {maint_need} days of maintainence, only {current_stock_dict['maint_time']} available.")
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
        print("-" * 60)
        fish_rev = species['price'] * demand 
        add_rev = current_stock_dict['cash']+fish_rev
        current_stock_dict['cash'] = add_rev
        display_stocks()

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
    print("-" * 60)
    standard = Nans_Hatchy.quarterly_payment 
    tech_payments = len(Nans_Hatchy.current_techs)*6000 ###find way to put in nans_hatchy #500 mulitpled by 9 weeks
    
    warehouse_fert = current_stock_dict['fert']*main_warehouse.costs.fertilizer_warehouse #is in liters so it is ok
    warehouse_feed = (current_stock_dict['feed']*1000)*main_warehouse.costs.feed_warehouse #multiply by 1000 to convert to grams
    warehouse_salt = (current_stock_dict['salt']*1000)*main_warehouse.costs.salt_warehouse #multiply by 1000 to convert to grams
    
    total_warehouse = warehouse_fert + warehouse_feed + warehouse_salt
    total_payments = standard + tech_payments + total_warehouse
    print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Warehouse Costs: £{total_warehouse:.2f}")
    
    current_stock_dict['cash'] -= total_payments
    print("Updated Stocks after Payments")
    display_stocks()
    cash_balance = current_stock_dict['cash']
    make_pretty(f"Cash Balance: £{cash_balance:.2f}")
    

#Now restock your supples : 
#Display inventory in the two warehouses 
#function to see how much is left 
#if amount less > than aux.amount (meaning aux warehouse still has things inside)
    #minus off remainder from main warehouse 
#if amount less < aux.amount (meaning aux warehouse is empty )

#depreciation happenings: 
def Depreciate ():
    current_stock_dict['fert']*=(1-main_warehouse.costs.fertilizer_depreciation) #using main warehouse since does not matter where from
    current_stock_dict['feed']*= (1-main_warehouse.costs.feed_depreciation)
    current_stock_dict['salt']*= (1-main_warehouse.costs.salt_depreciation)

def Warehouse_left():
    #Going by the logic that auxillary will be drained LAST
    if current_stock_dict['fert'] >= aux_warehouse.fert_amount: #meaning that the aux warehouse will be full, does not change
        main_warehouse.fert_amount = current_stock_dict['fert'] - aux_warehouse.fert_amount #so calculate what is left in main warehosue
    else: #current_stock_fict['fert'] <= aux_warehouse.fert.amount
        aux_warehouse.fert_amount = current_stock_dict['fert'] #else main is empty, whatever is left is in the aux
        main_warehouse.fert_amount = 0 #assign 0 to main
   
    if current_stock_dict['feed'] >= aux_warehouse.feed_amount:
        main_warehouse.feed_amount = current_stock_dict['feed'] - aux_warehouse.feed_amount
    else:
        aux_warehouse.feed_amount = current_stock_dict['feed']
        main_warehouse.feed_amount = 0 
    
    if current_stock_dict['salt'] >= aux_warehouse.salt_amount:
        main_warehouse.salt_amount = current_stock_dict['salt'] - aux_warehouse.salt_amount
    else:
        main_warehouse.salt_amount = current_stock_dict['salt']
        main_warehouse.salt_amount = 0
    
    print("-" * 60)
    print("Your leftover supplies have depreciated! Here is what you have left now:")
    print(f"Fertilizer left in Main Warehouse: {main_warehouse.fert_amount:.2f}")
    print(f"Fertilizer left in Auxillary Warehouse: {aux_warehouse.fert_amount:.2f}")
    print(f"Feed left in Main Warehouse: {main_warehouse.feed_amount:.2f}")
    print(f"Feed left in Auxillary Warehouse: {aux_warehouse.feed_amount:.2f}")
    print(f"Salt left in Main Warehouse: {main_warehouse.salt_amount:.2f}")
    print(f"Salt left in Auxillary Warehouse: {aux_warehouse.salt_amount:.2f}")


#Choose which vendor to buy from
#Print Prices

def restocker():
    print("It's time to restock!")
    #Fertilizer, liters
    fert_restock_amount = (main_warehouse.fertilizer_capacity - main_warehouse.fert_amount) + (aux_warehouse.fertilizer_capacity-aux_warehouse.fert_amount) 
    while True:
        restock_fertilizer = input(f'Where would you like to purchase your Fertilizer from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}') #since the names too long
        if restock_fertilizer == '1':
            fert_price = fert_restock_amount * Slippery.fertilizer_cost
            print(f"Paid £{fert_price:.2f} to {Slippery.name}")
            break
        elif restock_fertilizer == '2':
            fert_price = fert_restock_amount * Scaly.fertilizer_cost
            print(f"Paid £{fert_price:.2f} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') #now how to go back?
    feed_restock_amount = (main_warehouse.feed_capacity - main_warehouse.feed_amount) + (aux_warehouse.feed_capacity-aux_warehouse.feed_amount) 
    while True:
        restock_feed = input(f'Where would you like to purchase your Feed from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_feed == '1':
            feed_price = feed_restock_amount * Slippery.feed_cost 
            print(f"Paid £{feed_price:.2f} to {Slippery.name}")
            break
        elif restock_feed == '2':
            feed_price = feed_restock_amount * Scaly.feed_cost 
            print(f"Paid £{feed_price:.2f} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') #now how to go back?
    salt_restock_amount = (main_warehouse.salt_capacity - main_warehouse.salt_amount) + (aux_warehouse.salt_capacity-aux_warehouse.salt_amount) 
    while True:
        restock_salt = input(f'Where would you like to purchase your Salt from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_salt == '1':
            salt_price = (salt_restock_amount) * Slippery.salt_cost 
            print(f"Paid £{salt_price:.2f} to {Slippery.name}")
            break
        elif restock_salt == '2':
            salt_price = (salt_restock_amount) * Scaly.salt_cost
            print(f"Paid £{salt_price:.2f} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') 
    
    #manual restock all items (since it is fully replenished now)
    main_warehouse.fert_amount = main_warehouse.fertilizer_capacity
    main_warehouse.feed_amount = main_warehouse.feed_capacity
    main_warehouse.salt_amount = main_warehouse.salt_capacity
        
    restock_price = fert_price+feed_price+salt_price
    current_stock_dict['cash'] -= restock_price
    #add supplies into restock also: 
    #manually assign that its back at max? #better to assign the actual value restocked?? 
    cash_balance = current_stock_dict['cash']
    make_pretty(f"Cash Balance: £{cash_balance:.2f}")

#Quarter Loopy
def Quarter():
    while True: 
        try:
            quarters = int(input('Please type in how many quarters Fish Tycoon will run for:'))
            if quarters <= 0:
                print("You need to run at least one quarter")
            else:
                break
        except ValueError:
            print("It needs to be a number")
    
    current_q = 1        
    
    while quarters > 0:

        make_pretty(f"Quarter {current_q} begins:")
        # print("-" * 40)
        # print(f"Quarter {current_q} begins:")
        
        #Adding the Techs
        Hatchery.Tech_Roster(Nans_Hatchy)
        Hatchery.Tech_Again(Nans_Hatchy)
        Hatchery.Tech_display(Nans_Hatchy)

        #Update stocks now that techs are hired~
        Current_stocks() #update the stocks first
        print("Your resources for the year:")
        display_stocks()

        #Selling fishes!
        make_pretty("Time to Sell Fish!!")
        Deplete_stocks() #selling fish
        Payments()
        #put in a if/else checkpoint, if currently in the negatives, bankrupt! bad ending
        
        if current_stock_dict['cash'] <0:
            print("Oh no! You could not pay your Technicians! \nThey unionized and filed a lawsuit. \nYou went bankrupt and the hatchery closed.")
            make_pretty("Bad Ending. Game Over")
            break
        
        #Update stocks!
        Depreciate()
        Warehouse_left()

        make_pretty("Rrepare for the next quarter. Restock!")
        print('These two vendors work with you:')
        Slippery.display()
        Scaly.display()
        restocker()

        if current_stock_dict['cash'] < 0:
            print("Oh no! You couldnt pay the vendors! \nThey boycotted you so your fishes died. \nThe hatchery had to close down.")
            make_pretty("Bad Ending. Game Over")
            break
        print(f'Congrats! The hatchery survived the Quarter')
        if quarters == 1:
            print("Good job! Your hatchery survived. Go forth and raise fishes")
            make_pretty("Good Ending. Game Over.")
        quarters -= 1 #reduce number of loops left 
        current_q += 1 #add number for current quarter

print("Welcome to Fish Tycoon, Please Try Not to Go Bankrupt.")
print("Have fun!")
print(f"You start with £{Nans_Hatchy.cash}")
display_stocks()

Quarter()
print("Thanks for playing! Have a nice day")


        