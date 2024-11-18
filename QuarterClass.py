###remember to change all the quaters to QUARTER with and R. RRRRRR.
#### also reminder to edit and convert all the units afterwards 

from FishClass import Fish
from WarehouseClass import Warehouse
from TechicianClass import Technician
from VendorClass import Vendor
from HatcheryClass import Hatchery

class Quarter:
    current_stock_dict = {'maint_time':0, 'fert':0, 'feed':0, 'salt':0, 'cash':0}

    def Current_stocks():
        Quarter.Current_stock_dict['maint_time']=len(Hatchery.current_techs)*45 #45 days of work per person

        #Adding sum of items in the warehouse 
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Fert)
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Feed)
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Salt)
    

    def deplete_stocks(fishy):
        
        for fish in fishy: 

            demand = Fish.fertilizer.demand
            
            fert_need = Fish.fertilizer * demand
            feed_need = Fish.feed * demand
            salt_need = Fish.salt * demand

            if Quarter.current_stock_dict['fert'] >= fert_need:
                new_fert_value = Quarter.current_stock_dict['fert'] - fert_need
                Quarter.current_stock_dict['fert'].append(new_fert_value)
                print(f"{fish.species}: {fert_need}ml fertilizer used.")
            else:
                print(f"Not enough fertilizer for {fish.species}. {fert_need}ml needed, only {Quarter.current_stock_dict['fert']}ml available.")

            if Quarter.current_stock_dict['feed'] >= feed_need:
                new_feed_value=Quarter.current_stock_dict['feed'] - feed_need
                Quarter.current_stock_dict['feed'].append(new_feed_value)
                print(f"{fish.species}: {feed_need}kg feed used.")
            else:
                print(f"Not enough feed for {fish.species}. {feed_need}kg needed, only {Quarter.current_stock_dict['feed']}kg available.")

            if Quarter.current_stock_dict['salt'] >= salt_need:
                new_salt_value= Quarter.current_stock_dict['salt'] - salt_need
                print(f"{fish.species}: {salt_need}kg salt used.")
            else:
                print(f"Not enough salt for {fish.species}. {salt_need}kg needed, only {Quarter.current_stock_dict['salt']}kg available.")

    #ok so: fish have fert, feed, salt
    #1st type of fish: input number being sold:
    #function loop starts: number of fish * fert 
    #if enough fert in warehouses, move to next item, feed. 
    #if enough feed in warehouses, move to next item 
    #if enough salt in warehouses, move to next item
        pass
    
    def payments():
        standard = 1500
        tech_payments = len(Hatchery.current_techs)*4500 #500 mulitpled by 9 weeks 