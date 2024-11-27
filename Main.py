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
    """
    Function that loops through the list of fish, meet demands and then deplete stocks accordingly
    
    Asks user input many of each fish to sell, to a maximum of the demand.
    Checks if supplies are met, and if labour need is met
    Factors for availability of specialized technician.
    If all conditions met, stocks are minused from the dictionary. 
    If not all conditions met, does not minus, unable to sell.
    Moves on to next fish in the list. 
    """
    #for loop to go through each of the 6 fishes 
    for species in Fishies: 

        #Lines to seperate each fish section, for clarity  
        print("-" * 60)
        #Asks user for number of fish to try raise and sell. No answer/invalid answer means default 
        user_demand = input(f"How many {species['species']} are you selling this quarter? \nDon't enter anything for default demand of {species['demand']}").strip()
        #If user does not enter anything
        if user_demand == '':
            #create new variable 'demand' to assign how many fish are being sold 
            #nothing entered means demand = default
            demand = species['demand']
            #output to user
            print('Default selected') 
        else: 
            #try except for error handling
            try:
                #convert to integer to perform functions
                #assign demand variable to user input. 
                #If doesnt meet error conditions, this will be the selected number
                demand = int(user_demand) 
                #if value entered under zero
                if int(demand) < 0:
                    #Invalid response
                    print('It needs to be a positive number. Default demand selected.')
                    #automatic selection of default 
                    demand = species['demand']
                #If user selects more fish to sell than demand
                #convert to integer    
                elif int(user_demand) > species['demand']:
                    print('You tried to sell alot of fish! But there were no takers. You sold the default')
                    #Fish sold = demand only 
                    demand = species['demand']
            #error handling for non-number answers 
            except ValueError:
                #invalid response
                print('It needs to be a number. Default demand selected')
                #automatic selection of default
                demand = species['demand']
         #Feedback to user that their value was selected 
        print(f'Selected {demand}')

        #determine how much of each item is needed 
        #muiltiply each by demand  
        fert_need = species['fertilizer'] * demand
        feed_need = species['feed'] * demand
        salt_need = species['salt'] * demand
        maint_need = species['maint_time'] * demand

        #Begin if else check statements for checking stock availability

        #If the current amount of fert is above the need,
        if current_stock_dict['fert'] >= fert_need:
            #Let user know fertilizer amount enough
            print('Fertilizer need met.')
        #If the current amount is not enough
        else:
            #Let user know they did not sell the fish
            print(f"The {species['species']} died from lack of poor air quality! \n{species['species']} need {fert_need}liters of fertilizer, only {current_stock_dict['fert']}l available.")
            #Continue statement to ignore the rest and move on to next fish
            continue
        
        #If the current amount of feed is above the need,
        if current_stock_dict['feed'] >= feed_need:
            #Let user know feed amount enough
            print("Feed need met.")
        #If the current amount is not enough
        else:
            #Let user know they did not sell the fish
            print(f"The {species['species']} died from malnourishment! \n{species['species']} need {feed_need}kg of feed, only {current_stock_dict['feed']}kg available.")
            #Continue statement to ignore the rest and move on to next fish
            continue
        
        #If the current amount of salt is above the need,
        if current_stock_dict['salt'] >= salt_need:
            #Let user know salt amount enough
            print("Salt need met")
        #If the current amount is not enough
        else:
            #Let user know they did not sell the fish
            print(f"The {species['species']} died from reverse osmosis! \n{species['species']} need {salt_need}kg of salt, only {current_stock_dict['salt']}kg available.")
            #Continue statement to ignore the rest and move on to next fish
            continue
        
        #Move on to calculating maintenence 
        #Store the inital time each tech has, incase demand is not met
        time_start = {tech: tech.labourtime for tech in Nans_Hatchy.current_techs}
        #Assign new variable for the time left 
        time_left = maint_need #ensure the original time stays there
        #Loop through each technician
        for tech in Nans_Hatchy.current_techs:
            #Find if the tech has a specialty using tech.specialty = fish species
            if tech.specialty == species['species']: 
                #New maintainence time, 2/3 of original, rounded
                special_time = round(time_left*(2/3))
                #Check if technician has enough labour time left
                #If they have more than needed or just enough
                if tech.labourtime >= special_time:
                    #Minus all the time
                    tech.labourtime -= special_time
                    #No more maintainence time needed
                    time_left = 0
                    #Let user know
                    print(f"Specialized Technican can tend to {species['species']}.")
                    #Exit loop
                    break
                #If specialized tech cannot meet the need:
                else: 
                    #Minus off whatever the tech is able to do
                    special_time -= tech.labourtime
                    #Reduce Techicians available days to 0
                    tech.labourtime = 0
                    #convert special time back into normal
                    time_left = special_time/(2/3)
            
            #Time_left if there was no specialization
            #Also applies to Time_left after minus technicians time
            if time_left > 0:
                #loop though each techinician
                for tech in Nans_Hatchy.current_techs:
                    #If they have time available
                    if tech.labourtime > 0:
                        #If they have more than necessary time left
                        if tech.labourtime >= time_left:
                            #Reduce hours 
                            tech.labourtime -= time_left
                            #Time need is met, assign zero
                            time_left = 0  
                            #Let user know 
                            print('Maintaince was done by both Specialized and Normal Techs.')
                            #Exit loop
                            break
                        #If the tech doesnt have enough to cover
                        else:
                            #Minus what the tech can give
                            time_left -= tech.labourtime
                            #Technician hours are used up, assign zero
                            tech.labourtime = 0
                            #Function loops back to check next technician
            
            #If the fish still needs maintainence, 
            if time_left > 0:
                #Unable to meet conditions, let user know
                print(f"Your staff are overworked! {species['species']} need {maint_need} days of maintainence. There isnt enough help!")
                #Revert back to original labour days as unable to sell fish
                #Loop through the list of technicians
                for tech, starting_days in time_start.items():
                    #Assign back the inital values
                    tech.labourtime = starting_days
                    #Ignore the rest and move on to next fish
                    continue
        
        #Let user know how much of each item was used. 
        #Rounded to 2 dp
        print(f"{species['species']}: {fert_need:.2f}l fertilizer used.")
        print(f"{species['species']}: {feed_need:.2f}kg feed used.")
        print(f"{species['species']}: {salt_need:.2f}kg salt used.")

        #Update current stocks in dictionary
        #Current value - amount used 
        #Only gets here once all the checks are conducted above
        current_stock_dict['fert'] -= fert_need
        current_stock_dict['feed'] -= feed_need
        current_stock_dict['salt'] -= salt_need

        #Counts revenue for the fish sold
        #Line for calrity when viewing outputs
        print("-" * 60)
        #calculate revenue by muliplying by amount sold (demand)
        fish_rev = species['price'] * demand 
        #Update into dictionary
        current_stock_dict['cash']+=fish_rev
        #Inform user current stocks avilable
        print("Updated Stocks after selling")
        #Display function to display it
        display_stocks()

#Function to pay for everything in the quarter
def Payments():
    """
    Calcuate standard feeds, Technician fees, Warehouse Cost for each item in the Warehouse
    Calls all the items available and mulitplies by their costs
    """
    #Line for visual clarity
    print("-" * 60)
    #Quarterly payment, taken from Hatchery
    standard = Nans_Hatchy.quarterly_payment 
    #Payment for technicians, number * pay
    tech_payments = len(Nans_Hatchy.current_techs)*6000###find way to put in nans_hatchy #500 mulitpled by 9 weeks #[0]
    #Payments for fertilizer, feed, salt in inventory after quarter. Uses main_warehouse._ as both values are same.
    warehouse_fert = current_stock_dict['fert']*main_warehouse.costs.fertilizer_warehouse #Both values in liters
    warehouse_feed = (current_stock_dict['feed']*1000)*main_warehouse.costs.feed_warehouse #Cost is in grams, * by 1000 to convert 
    warehouse_salt = (current_stock_dict['salt']*1000)*main_warehouse.costs.salt_warehouse #Cost is in grams, * by 1000 to convert 
    
    #Add all three payment types from warehouse and assign variable
    total_warehouse = warehouse_fert + warehouse_feed + warehouse_salt
    #All all payments to be made and assign variable
    total_payments = standard + tech_payments + total_warehouse
    #Statement to inform user of amount payable
    print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Warehouse Costs: £{total_warehouse}")
    
    #Minus amount payable from cash in dictionary
    current_stock_dict['cash'] -= total_payments
    #Inform user of cash balance after payments
    make_pretty(f"Cash Balance:£{current_stock_dict['cash']}")
    
 
def Depreciate ():
    """ Function to calculate depreciation of each item in warehouse"""
    #Depreciation= 0.x. Amount remaining = 1-(depreciation)
    #run for all 3 items
    current_stock_dict['fert']*=(1-main_warehouse.costs.fertilizer_depreciation) #using main warehouse since same between two warehouses
    current_stock_dict['feed']*= (1-main_warehouse.costs.feed_depreciation)
    current_stock_dict['salt']*= (1-main_warehouse.costs.salt_depreciation)

def Warehouse_left():
    """ 
    Function to determine how much of each item (Fert, Feed, Salt) in Main & Aux Warehouses
    Goes by the logic that auxillary warehouse is drained last. 
    If, total of the item leftover is more than what was in aux, means nothing was draining from aux. 
    Therefore, minus off auxillary amoung from total leftover. 
    This is what is left in the main. 
    Else, if the amount leftover is less than what was in the aux, means everything left is in aux
    Main will be empty
    Using 'amount' instead of 'capacity' in order to prepare for an extension that allows incomplete restock.
    """
    #If else statement for each item (fert, feed, salt)
    
    #FERTILIZER
    #If current_stock_dict amount is more or equals to aux amount, aux is unchanged 
    #The rest of the current stock amount is allocated to main
    if current_stock_dict['fert'] >= aux_warehouse.fert_amount: 
        main_warehouse.fert_amount = current_stock_dict['fert'] - aux_warehouse.fert_amount #so calculate what is left in main warehosue
    #Else, leftover amount is less than aux amount 
    #Meaning everything left over is in aux
    #Assign zero to main warehouse 
    else: 
        aux_warehouse.fert_amount = current_stock_dict['fert']
        main_warehouse.fert_amount = 0 #assign 0 to main
    
    #FEED
    #If current_stock_dict amount is more or equals to aux amount, aux is unchanged 
    #The rest of the current stock amount is allocated to main
    if current_stock_dict['feed'] >= aux_warehouse.feed_amount:
        main_warehouse.feed_amount = current_stock_dict['feed'] - aux_warehouse.feed_amount
    #Else, leftover amount is less than aux amount 
    #Meaning everything left over is in aux
    #Assign zero to main warehouse 
    else:
        aux_warehouse.feed_amount = current_stock_dict['feed']
        main_warehouse.feed_amount = 0 

    #SALT
    #If current_stock_dict amount is more or equals to aux amount, aux is unchanged 
    #The rest of the current stock amount is allocated to main
    if current_stock_dict['salt'] >= aux_warehouse.salt_amount:
        main_warehouse.salt_amount = current_stock_dict['salt'] - aux_warehouse.salt_amount
    #Else, leftover amount is less than aux amount 
    #Meaning everything left over is in aux
    #Assign zero to main warehouse 
    else:
        main_warehouse.salt_amount = current_stock_dict['salt']
        main_warehouse.salt_amount = 0
    
    #Print out leftover in warehouse for user to see
    #Line for visual clarity
    print("-" * 60)
    print("Your leftover supplies have depreciated! Here is what you have left now:")
    print(f"Fertilizer left in Main Warehouse: {main_warehouse.fert_amount:.2f}liters")
    print(f"Fertilizer left in Auxillary Warehouse: {aux_warehouse.fert_amount:.2f}liters")
    print(f"Feed left in Main Warehouse: {main_warehouse.feed_amount:.2f}kg")
    print(f"Feed left in Auxillary Warehouse: {aux_warehouse.feed_amount:.2f}kg")
    print(f"Salt left in Main Warehouse: {main_warehouse.salt_amount:.2f}kg")
    print(f"Salt left in Auxillary Warehouse: {aux_warehouse.salt_amount:.2f}kg")

def restocker():
    """
    Function to restock supplies 
    Display costs of each warehouse. 
    Allow user to choose who to buy which item from
    Charge user (minus cash) after all is done
    """
    #Let user know what is going on
    print("It's time to restock!")
    #Fertilizer, liters
    #Calculate how much is needed to restock fert
    #Total capacity minus what is inside currently
    #Add together and assign a restock amount
    fert_restock_amount = (main_warehouse.fertilizer_capacity - main_warehouse.fert_amount) + (aux_warehouse.fertilizer_capacity-aux_warehouse.fert_amount) 
    #while true loop for error handling
    while True:
        #As user to select vendor
        restock_fertilizer = input(f'Where would you like to purchase your Fertilizer from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}') #since the names too long
        #User selects option 1
        if restock_fertilizer == '1':
            #calculate fertilizer price based on Vendor 1
            fert_price = fert_restock_amount * Slippery.fertilizer_cost
            #inform user of how much paid
            print(f"Paid £{fert_price:.2f} to £{Slippery.name}")
            #exit while loop and move on with function
            break
        elif restock_fertilizer == '2':
            #calculate fertilizer price based on Vendor 2
            fert_price = fert_restock_amount * Scaly.fertilizer_cost
            #inform user of how much paid
            print(f"Paid £{fert_price:.2f} to {Scaly.name}")
            #exit while loop and move on with function
            break
        #invalid response
        else: 
            #loop back until accepted answer
            print('Type a number I understand please') 
    feed_restock_amount = (main_warehouse.feed_capacity - main_warehouse.feed_amount) + (aux_warehouse.feed_capacity-aux_warehouse.feed_amount) 
    while True:
        restock_feed = input(f'Where would you like to purchase your Feed from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_feed == '1':
            #calculate fertilizer price based on Vendor 1
            feed_price = feed_restock_amount * Slippery.feed_cost 
            #inform user of how much paid
            print(f"Paid £{feed_price:.2f} to {Slippery.name}")
            #exit while loop and move on with function
            break
        elif restock_feed == '2':
            #calculate fertilizer price based on Vendor 2
            feed_price = feed_restock_amount * Scaly.feed_cost 
            #inform user of how much paid
            print(f"Paid £{feed_price:.2f} to {Scaly.name}")
            #exit while loop and move on with function
            break
        #invalid response
        else: 
            print('Type a number I understand please') #Loop back until answer can be accepted
    salt_restock_amount = (main_warehouse.salt_capacity - main_warehouse.salt_amount) + (aux_warehouse.salt_capacity-aux_warehouse.salt_amount) 
    while True:
        restock_salt = input(f'Where would you like to purchase your Salt from? \n Enter [1] for {Slippery.name} and [2] for {Scaly.name}')
        if restock_salt == '1':
            #calculate fertilizer price based on Vendor 1
            salt_price = (salt_restock_amount) * Slippery.salt_cost 
            #inform user of how much paid
            print(f"Paid £{salt_price:.2f} to {Slippery.name}")
            #exit while loop and move on with function
            break
        elif restock_salt == '2':
            #calculate fertilizer price based on Vendor 2
            salt_price = (salt_restock_amount) * Scaly.salt_cost
            #inform user of how much paid
            print(f"Paid £{salt_price:.2f} to {Scaly.name}")
            #exit while loop and move on with function
            break
        #invalid response
        else: 
            print('Type a number I understand please') #loop back until answer can be accepted
    
    #manual restock all items (since it is fully replenished now)
    #fert amount = fert capacity, full replenish
    #applied to Main and Aux, Fert, Feed, Salt
    main_warehouse.fert_amount = main_warehouse.fertilizer_capacity
    main_warehouse.feed_amount = main_warehouse.feed_capacity
    main_warehouse.salt_amount = main_warehouse.salt_capacity
    aux_warehouse.fert_amount = aux_warehouse.fertilizer_capacity
    aux_warehouse.feed_amount = aux_warehouse.feed_capacity
    aux_warehouse.salt_amount = aux_warehouse.salt_capacity

    #Add all the prices that were quoted to user    
    restock_price = fert_price+feed_price+salt_price
    #Minus from cash balance
    current_stock_dict['cash'] -= restock_price
    #Display to user
    make_pretty(f"Cash Balance:£{current_stock_dict['cash']:.2f}") #remove

def Quarter():
    """ Loop to comprise all the functions that occur in a quarter """
    #While true for error handling, must be an integer and above zero
    while True: 
        try:
            #Asks for user input for number of quarters to run simulation
            quarters = int(input('Please type in how many quarters Fish Tycoon will run for:'))
            #Unable to go less than 0
            if quarters <= 0:
                #Informs user, brings back to loop
                print("You need to run at least one quarter")
            else:
                #If acceptable, break out of loop
                break
        #If not number
        except ValueError:
            #loops back
            print("It needs to be a number")
    
    #define a variable for the current quarter
    current_q = 1        
    
    #Begin a big while loop for the number of quarters selected
    while quarters > 0:

        #Displau start of each quarter
        make_pretty(f"Quarter {current_q} begins:")
        
        #Call from Hatchery Class:
        #Adding technicians (Tech Roster)
        Hatchery.Tech_Roster(Nans_Hatchy)
        #Option to make ammendments
        Hatchery.Tech_Again(Nans_Hatchy)
        #Display who has been hired
        Hatchery.Tech_display(Nans_Hatchy)

        #Update stocks now that techs are hired
        Current_stocks() #update the stocks first
        #Display to user what they  have available
        print("Your resources for the year:")
        #Function to display
        display_stocks()

        #Selling fishes!
        make_pretty("Time to Sell Fish!!")
        #Function to let user input fishes to sell
        #Deplete stocks accordingly
        Deplete_stocks() #selling fish
        #Making payments for warehouse and others
        Payments()
        
        #if/else checkpoint, if currently in the negatives, bankrupt! bad ending
        if current_stock_dict['cash'] <0: #if negative
            #Let user know
            print("Oh no! You could not pay your Technicians! \nThey unionized and filed a lawsuit. \nYou went bankrupt and the hatchery closed.")
            #Game over
            make_pretty("Bad Ending. Game Over")
            #Break out of loop
            break
        
        #If survived
        #Update stocks!
        Depreciate()
        #Function to let the warehosue items depreciate
        Warehouse_left()
        #Function to calcuate what is left in the warehouse

        #Display for next portion, to restock
        make_pretty("Rrepare for the next quarter. Restock!")
        #Inform users their options
        print('These two vendors work with you:')
        #Displau vendor 1
        Slippery.display()
        #Displau vendor 2
        Scaly.display()
        #Function for users to restock
        restocker()

        #Bankrup checkpount, if in negatives:
        if current_stock_dict['cash'] < 0:
            #Inform user
            print("Oh no! You couldnt pay the vendors! \nThey boycotted you so your fishes died. \nThe hatchery had to close down.")
            #Game over
            make_pretty("Bad Ending. Game Over")
            #Exit loop
            break
        #If in positives
        print(f'Congrats! The hatchery survived the Quarter')
        #If this is the last loop (quarters is 1, will lead to 0 thus loop break in next round)
        if quarters == 1:
            #aim of game as been achieed
            print("Good job! Your hatchery survived. Go forth and raise fishes")
            make_pretty("Good Ending. Game Over.") #game over
        #reduce number of loops left (for the while loop > 0 criteria)
        quarters -= 1 
        #add number for current quarter
        current_q += 1 


##### FINALLY, THE ACTUAL PLAYTHROUGH:

#Opening statement
print("Welcome to Fish Tycoon, Please Try Not to Go Bankrupt.")
print("Have fun!")
#Let user know starting money
print(f"You start with £{Nans_Hatchy.cash}")

#Game loop function
Quarter()
#Once everything is over, goodbye message
print("Thanks for playing! Have a nice day")


        