#Import all the classes:
from FishClass import Fish
from WarehouseClass import Warehouse
from VendorClass import Vendor
from HatcheryClass import Hatchery

#Start with Initiating the Instances 

#Initiating each fish by following the Fish Class Template:
#fertilizer, feed, salt, maintainence days, demand, price
#.__dict__ to changed into a dictionary for ease of looping through
#units are ml,kg,kg,days, not applicable to demand, pounds
fin = Fish('Clef Fins',100.0,12,2,2.0,25,250).__dict__ 
snapper = Fish('Timpani Snapper', 50.0, 9, 2, 1.0, 10, 350).__dict__
brim = Fish('Andalusian Brim', 90.0, 6, 2, 0.5, 15, 250).__dict__
cod = Fish('Plagal Cod', 100.0, 10, 2, 2.0, 20, 400).__dict__
flounder = Fish('Fugue Flounder', 200.0, 12, 2, 2.5, 30, 550).__dict__
bass = Fish('Modal Bass', 300.0, 12, 6, 3.0, 50, 500).__dict__

#create list of fish dictionaries with each fish type
Fishies = [fin,snapper,brim,cod,flounder,bass]

#For loop to convert all the ml to liters, for convience later
for fish in Fishies:
    #for fertilizer in fish list, divide by 1000 to go from ml to l
    fish['fertilizer'] = fish['fertilizer']/1000

#Instanciate the two warehouses
#Fert, feed, salt, amt, capacity
#units: liters, kg, kg
main_warehouse = Warehouse('Main',20,20,400,400,200,200)
aux_warehouse = Warehouse('Aux',10,10,200,200,100,100)

#Istanciate the two vendors
#Fert, Feed, Salt
#units: pound per liter, pound per kg, pound per kg
Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

#Insanciate Hatchery, 'Nans' Hatchery
Nans_Hatchy = Hatchery('supplies', 10000)

#Function: Make Pretty 
def make_pretty(title):
    """ Function to make headers and titles look nice in a box """
    print(f"\n{'=' * 60}")
    print(f"{title.center(60)}")
    print(f"{'=' * 60}")

#Create a dictonary of the things that flow within the hatchery
#Key: maint_time for maintainence time of the techniciians, Value: maint_time from the hatchery class instance
#Key: fertilizer, feed, salt, value yet added later
#Key: Cash for cash in hatchery, value: value from hatchery class instance
current_stock_dict = {'maint_time':Nans_Hatchy.current_techs, 'fert':0, 'feed':0, 'salt':0, 'cash':Nans_Hatchy.cash} #inside a class? 

#Function: Displaying the stocks in the Hatchery right now
def display_stocks():
    """ 
    Nicely displays the inventory in current_stock_dict
    Loop throught the current stock dictionary to get each technician's name and labour time left
    Then displays the fert, feed, salt and cash in the dictionary
    """
    #for loop for each tehcnician in the hatchery.current_techs instances
    for tech in current_stock_dict['maint_time']:
        #print out the technician name and labour time left
        print(f"Technician Name: {tech.name}, Labour Days: {tech.labourtime}")
    #print fertilizer amount, liters, rounded to 2dp
    print(f"Fertilizer Available: {current_stock_dict['fert']:.2f} liters")
    #print feed amount, kg, rounded to 2dp
    print(f"Feed Available: {current_stock_dict['feed']:.2f} kg")
    #print salt amount, kg, rounded to 2dp
    print(f"Salt Available: {current_stock_dict['salt']:.2f} kg")
    #print cash amound, pounds, rounded to 2 dp
    print(f"Cash Balance: £{current_stock_dict['cash']:.2f}")            

#Function to update stocks in warehouse
def Current_stocks():
    """
    Updates the current amount of stocks in the dictionary
    Loops through technicains in the list and adds the starting number of labour days
    Then adds the values of what is inside the main and auxillary warehohouse for the other items
    """
    #Append to dictionary number of labour days available
    #loop through each tech
    for tech in current_stock_dict['maint_time']: 
        #assign the value of the  labour days to current available time
        tech.labourtime = tech.labourdays #this way to reset the labour time each loop(quarter)

    #Adding sum of items in the warehouse 
    #Add via warehouse class for main and aux, allow to add option for not replenishing fully 
    #Add current amount in main and aux warehosue for fertilizer
    current_stock_dict['fert'] = main_warehouse.fert_amount + aux_warehouse.fert_amount #allows for not full replenishing
    #Add current amount in main and aux warehosue for feed
    current_stock_dict['feed'] = main_warehouse.feed_amount + aux_warehouse.feed_amount
    #Add current amount in main and aux warehosue for salt
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
        time_start = {tech: tech.labourtime for tech in Nans_Hatchy.current_techs}
        time_left = maint_need
        for tech in Nans_Hatchy.current_techs:
            #if the instance in tech.specialty = fish species
            if tech.specialty == species['species']: #need to assign value for each fish in this case 
                #find new maintainence time
                special_time = species['maint_time']*(2/3)
                special_time = round(time_left*(2/3))
                if tech.labourtime >= special_time:
                    tech.labourtime -= special_time
                    time_left = 0
                    break
                else: 
                    special_time -= tech.labourtime
                    tech.labourtime = 0
            
            if time_left > 0:
                for tech in Nans_Hatchy.current_techs:
                    if tech.labourtime > 0:
                        if tech.labourtime >= time_left:
                            tech.labourtime -= time_left
                            time_left = 0  
                            break
                        else:
                            time_left -= tech.labourtime
                            tech.labourtime = 0
            
            if time_left > 0:
                print(f"Your staff are overworked! {species['species']} need {maint_need} days of maintainence. There isnt enough help!")
                for tech, starting_days in time_start.items():
                    tech.labourtime = starting_days
                    continue


        new_fert_value = current_stock_dict['fert'] - fert_need
        current_stock_dict['fert'] = (new_fert_value)
        new_feed_value = current_stock_dict['feed'] - feed_need
        current_stock_dict['feed'] = (new_feed_value)
        new_salt_value = current_stock_dict['salt'] - salt_need
        current_stock_dict['salt'] = (new_salt_value)
        # new_maint_value = current_stock_dict['maint_time']-maint_need
        # current_stock_dict['maint_time'] = (new_maint_value)

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
    print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Warehouse Costs: £{total_warehouse}")
    
    current_stock_dict['cash'] -= total_payments
    print("Updated Stocks after Payments")
    display_stocks()
    make_pretty(f"Cash Balance:£{current_stock_dict['cash']}")
    

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
    print(f"Fertilizer left in Main Warehouse: {main_warehouse.fert_amount}")
    print(f"Fertilizer left in Auxillary Warehouse: {aux_warehouse.fert_amount}")
    print(f"Feed left in Main Warehouse: {main_warehouse.feed_amount}")
    print(f"Feed left in Auxillary Warehouse: {aux_warehouse.feed_amount}")
    print(f"Salt left in Main Warehouse: {main_warehouse.salt_amount}")
    print(f"Salt left in Auxillary Warehouse: {aux_warehouse.salt_amount}")


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
            print(f"Paid {fert_price} to {Slippery.name}")
            break
        elif restock_fertilizer == '2':
            fert_price = fert_restock_amount * Scaly.fertilizer_cost
            print(f"Paid {fert_price} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') #now how to go back?
    feed_restock_amount = (main_warehouse.feed_capacity - main_warehouse.feed_amount) + (aux_warehouse.feed_capacity-aux_warehouse.feed_amount) 
    while True:
        restock_feed = input(f'Where would you like to purchase your Feed from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_feed == '1':
            feed_price = feed_restock_amount * Slippery.feed_cost 
            print(f"Paid {feed_price} to {Slippery.name}")
            break
        elif restock_feed == '2':
            feed_price = feed_restock_amount * Scaly.feed_cost 
            print(f"Paid {feed_price} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') #now how to go back?
    salt_restock_amount = (main_warehouse.salt_capacity - main_warehouse.salt_amount) + (aux_warehouse.salt_capacity-aux_warehouse.salt_amount) 
    while True:
        restock_salt = input(f'Where would you like to purchase your Salt from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_salt == '1':
            salt_price = (salt_restock_amount) * Slippery.salt_cost 
            print(f"Paid {salt_price} to {Slippery.name}")
            break
        elif restock_salt == '2':
            salt_price = (salt_restock_amount) * Scaly.salt_cost
            print(f"Paid {salt_price} to {Scaly.name}")
            break
        else: 
            print('Type a number I understand please') 
    
    #manual restock all items (since it is fully replenished now)
    main_warehouse.fert_amount = main_warehouse.fertilizer_capacity
    main_warehouse.feed_amount = main_warehouse.feed_capacity
    main_warehouse.salt_amount = main_warehouse.salt_capacity
        
    restock_price = fert_price+feed_price+salt_price
    current_stock_dict['cash'] = current_stock_dict['cash'] - restock_price
    #add supplies into restock also: 
    #manually assign that its back at max? #better to assign the actual value restocked?? 
    make_pretty(f"Cash Balance:£{current_stock_dict['cash']}") #remove

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


        