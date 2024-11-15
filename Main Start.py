from FishClass import Fish
from WarehouseClass import Warehouse
from TechicianClass import Techician
from VendorClass import Vendor
from HatcheryClass import Hatchery

#Very rough plan. 
#Inputs
print("Welcome to Fish Tycoon, Please Try Not to Go Bankrupt.")
print("Have fun!")
#Import in Hatchery (hatchery class has everything) 

#Asks for number of quaters to run the cycle
quaters = input('Please type in the number of quaters to run this simulation for')

#How many technicians would you like to add or remove?
while True:
    technician_number=int(input('Please write the NUMBER of technicians you would like to hire'))
    for x in range (technician_number):
        #Technician names 
        tech_name = input('Please type the name of the technician you would like to hire')
        #if in dict or class of tech names, do nothing
        #else, all into dict or class 
        print(f"Hired {tech_name.title()}, Days of Work = 45, Total Payment = 500")
    break
#"Hired ___, Total Payment: 500x9, total days of working 5x9=45

#How many fish sold
#standardized amount 

#some function to calculate the costs per fish sold, loop until run out of any item then say insufficient 

#say say what was unsold 

#current supplies in warehouses

#current hatchery cash 

#Amount to pay for technicians: 4500 x number of technicians))
#Amount for utilities: 1500 
#Amount to pay for depreciation: ?? 
#Hashery cash - all these above = updated hashery amount 

#Choose which vendor to buy from
#Print Prices
restock_Fertilizer = input('Where would you like to purchase your Fertilizer from?')
Slippery.display()
Scaly.display()
restock_Feed = input('Where would you like to purchase your Feed from?')
restock_Salt = input('Where would you like to purchase your Salt from?')
#Display vendors (select 1 or 2) 
