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
class `Hatchery`

description of your code design, classes,
methods, and other key details. 

## How to Install and Run the Project
There are 5 files for this project in total: 
1. FishClass.py
2. WarehouseClass.py
3. HatcheryClass.py
4. VendorClass.py
5. main.py

Ensure all scripts are within the same folder. To run


### Runing the project
### Design Process 

Design Considerations

### [How to Use the Project]
## Example 




Questions: 

changes to be made:
new tech obj 
check ui, spacing etc

HELP!!

1. in payments: I hard coded the 6000 payment for tech bc it wont work, cant figure out why again. If warehouse works so should this?


ideas for extension: 
1. stock how much you want in the warehouse (but will this kill me? idk)
2. choice of warehouse expansion after 4 quarters, just increase the the max
3. technician:
when select technician, ask if specialize 

