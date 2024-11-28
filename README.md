# OX24006_EMATM0048
## GitHub Repository for SPDA Summative Submisson - Part 1 

## Fish Tycoon (Nan's Version)
#### Fish Tycoon is an interactive, text-based fishery simulator "game", where the user plays as the manager of the fishery. The aim of the game is to manage the Hatchery/Fishery by selecting staff (known as Technicians or Techs) to maintain the fish, then trying to sell said fish, while making sure they can pay for all their expensive. The objective of the game is to stay in constant profit, meaning dont go bankrupt. 

This readme file will explain the details of the simulation design by going through the classes, methods and other details. 

**Disclaimer, Fish Tycoon (Nan's Version) will be refered to as Fish Tycoon henceforth. It is not to be confused with Fish Tycoon, the real game, available online. Please dont copyright me, thanks. Enjoy.

## Introduction to the scripts
This simulation was done using Object Oriented Programming. It used used 4 main classes and a `main.py` file to execute. 

### A breif overview of how the simulation will run:
The user will first be asked to select the number of quarters they want to simulate. Afterwhich they will be asked how many technicians they would like to hire/fire. There is no given list of techs, the user chooses. In the extended version, the user is able to select a specialty for the technician when they hire them. This reduces the time a technician takes to maintain the fish. 

After this, the selling begins. Users are asked how many of each fish they want to sell, where there is a limit - the demand. Based on this, the hatchery will 'raise' these fish, and sell them. There are 4 things needed to raise a fish, fertilizer, feed, salt and technicians (in the form of maintainence days). If the hatchery has enough of each item, fish will be raised and sold accordingly. If there isnt enough, the fish will die, and that type of fish doesnt get sold. Luckily for the user, even if the fish dies, the simulation gives the user plot armour and the supplies don't get used. Knowing that they are running low on supplies, they can alter the number of the next type of fish they want to sell. 

Once the selling is done, the simulation will automatically process the hatchery's expenses, including warehouse (which is where the supplies are kept) and technician costs. Supplies left over also depreciate. After these are done, the user can restock their supplies. They are given the option between two different vendoes and may choose which items they want to purchase and from who. 

If at any point here the users goes bankrupt, its game over. If they do stay in surplus, they move on to the next quarter. They user is trying to get through each quarter. 

## Code Outline

### Classes 
`FishClass.py` contains a template of information on the fishes. This includes
class `Fish`
- Name
- Fertilizer need per fish
- Feed need per fish
- Salt need per fish
- Selling price per fish 
- Demand per fish

`WarehouseClass.py` contains the template of information on the two warehouses that the hatchery has 
class `Warehouse`
- Name
- Fert amount - refering to the amount of fertilizer in the warehouse at present 
- Fertilizer capacity, refering to the maximum amount of fertilizer the ware house can hold 
- Feed amount - refering to the amount of feed in the warehouse at present
- Feed capacity - refering to the maximum amount of feed the ware house can hold 
- Salt Amount - refering to the amount of salt in the warehouse at present
- Salt Capacity - refering to the maximum amount of salt the ware house can hold 
- Class within, named `Warehouse_Costs`:
    - Fertilizer depreciation 
    - Feed depreciation
    - Salt depreciation
    - Cost of keeping fertilizer in the warehouse 
    - Cost of keeping feed in the warehouse
    - Cost of keeping salt in the warehouse
*Deisgn Choices* 
Here, feed amount and feed capacity were seperated. This was done with the intention of being able to add an extension that allows the user to choose how much to stock up the warehouse. 
Warehouse_Costs was put as a sub class as the information within remained the same for both warehouses.

`VendorClass.py` contains the template of information on the vendors 
class `Vendor`
- Name
- Fertilizer cost 
- Feed cost
- Salt cost

It also contains a method to display the costs to show the user.

`HatcheryClass.py`
class `Hatchery` - this has self, supplies and cash
Class will be initialized in `main.py` using:
Hatchery(name of hatchery, supples, amount of starting cash)

class `Technician` -  name, specialty and days of work, it is meant to be editable. An empty technican class is also initialized at the begining.  

Within this class there are two display methods
- `Tech_display`  for displaying the technicians after being hired 
- `Tech_names` for displaying the technicians before the choosing process 

And there are two functions for the technician hiring process 
- `Tech_Roster` : After describing the hiring process to the user, it asks for how many technicians to hire. 
    - Features: Error handling for non integer values, checking that there is at least 1 and less than 5 techs 
    - Extension: allows user to choose a specialty by fish.
    - Note: user here is allowed to name their technicians anything, even numbers.
- `Tech_Again` : simple if else to allow user to make changes to the technicians. This was done incase the user wanted to both hire and fire in the same cycle.

These are the only two loops that are defined inside a class as will be instanciated by the users inputs. 

`main.py`
This is where eerythign else is occuring. First it imports all the other scripts.

Step 1: Class Initialisation
Fishes types instanciated. The fishes, after initialization is formatted as a list of dictionaries. Handling of the different units is also done here.  
Warehouse instanciated. 
Vendors instanciated. 
Dictionary that contains the things that can change within the warehouse is also created, called `current_stock_dict`

Step 2: Defining functions 
1.  `make_pretty()` Simple function that keeps headers and titles in a nice box. Using this as the output and print statements can accumulate and confuse the user. 
2. `display_stocks()` Nicely displays the inventory in current_stock_dict. For users referece
3. `Current_stocks()` Updates the current amount of stocks in the dictionary 
4. `Deplete_stocks()` Function that loops through the list of fish, meet demands and then deplete stocks accordingly. This function is part of the main selling process, and takes in the users inputs, calculate how much supplies are needed. The sales pass/fail based on the calculations.
5. `Payments()` Calcuate standard fees, Technician fees, Warehouse Cost for each item left in the Warehouse. 
6. `Depreciate()` Calculate depreication amount of each item in the warehouse
7. `Warehouse_left()`  Function to determine how much of each item (Fert, Feed, Salt) in Main & Aux Warehouses. Because the values were not counted sepertely when looking at the warehouses during stocking/depletion, we take the logic here that auxillary is drained last. Calculations are made accordingly to this. Returns the amounts left in the warehouses.
8. `restocker()` Allows user to select which warehosue they want to restock each item from. User is charged after all the decisions are made. Currently, there is only the option of fully restocking, despite having preparations for custom stocking. The warehouses are returned to their max capacity. 
9. `Quarter()` this is the main function that orders all the occurances wihtin the quarter. Takes the value the user wants (number of quarters) and runs accordingly. There are two checkpoints for bankruptcy. First is after `Payments()` and the next is after `restocker()`. 


## How to Install and Run the Project
There are 5 files for this project in total: 
1. FishClass.py
2. WarehouseClass.py
3. HatcheryClass.py
4. VendorClass.py
5. main.py

Ensure all scripts are within the same folder. 

Run `main.py`

### Design Process and Considerations

The simulation was intended to be run similarly to a game, where there is a good and bad ending, with as many user friendly additions as possible - although it is admittedlty quite difficult to win the game. 

Considerations for extended version was 
1. Custom warehouse restocking 
2. Having 'lives', which means taking a loan if the user went bankrupt

## Github Repository:
https://github.com/nandikaL/OX24006_EMATM0048.git

## Main and Extension Packages 
**Main** 
Main package is the standard run of the simulator, with no technician specialty. 
**Extended-Version**
The main difference between this and main is the technician specialties. This occurs in HatcheryClass and main.py

switing using git branching:
`git checkout main`
`git checkout Extended-Version`



